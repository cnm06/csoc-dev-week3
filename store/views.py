from django.shortcuts import render
from django.shortcuts import get_object_or_404
from store.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import django
# Create your views here.


def index(request):
    return render(request, 'store/index.html')


def bookDetailView(request, bid):
    template_name = 'store/book_detail.html'
    context = {
        # set this to an instance of the required book
        'book': Book.objects.get(id=bid),
        'num_available': None,  # set this 1 if any copy of this book is available, otherwise 0
    }
    # START YOUR CODE HERE
    try:
        tmp = BookCopy.objects.filter(book=bid, status=True)
        context['num_available'] = len(tmp)
    except:
        context['num_available'] = 0
    return render(request, template_name, context=context)


def bookListView(request):
    template_name = 'store/book_list.html'

    get_data = request.GET
    # START YOUR CODE HERE
    books = Book.objects.all()
    try:
        qtitle = get_data['title']
        books = books.filter(title__contains=qtitle)
    except:
        pass
    try:
        qauthor = get_data['author']
        books = books.filter(author__contains=qauthor)
    except:
        pass
    try:
        qgenre = get_data['genre']
        books = books.filter(genre__contains=qgenre)
    except:
        pass
    context = {
        # set here the list of required books upon filtering using the GET parameters
        'books': books,
    }
    return render(request, template_name, context=context)


@login_required
def viewLoanedBooks(request):
    template_name = 'store/loaned_books.html'
    userid = request.user
    context = {
        'books': BookCopy.objects.filter(borrower=userid),
    }
    '''
    The above key books in dictionary context should contain a list of instances of the
    bookcopy model. Only those books should be included which have been loaned by the user.
    '''
    # START YOUR CODE HERE

    return render(request, template_name, context=context)


@csrf_exempt
@login_required
def loanBookView(request):
    response_data = {
        'message': "failiure",
    }
    '''
    Check if an instance of the asked book is available.
    If yes, then set message to 'success', otherwise 'failure'
    '''
    # START YOUR CODE HERE
    book_id = request.POST['bid']  # get the book id from post data
    for obj in BookCopy.objects.filter(book=book_id):
        if obj.status == True:
            BookCopy.objects.filter(id=obj.id).update(
                borrow_date=django.utils.timezone.now(), status=False, borrower=request.user)
            response_data['message'] = 1
            break
    return JsonResponse(response_data)


'''
FILL IN THE BELOW VIEW BY YOURSELF.
This view will return the issued book.
You need to accept the book id as argument from a post request.
You additionally need to complete the returnBook function in the loaned_books.html file
to make this feature complete
'''


@csrf_exempt
@login_required
def returnBookView(request):
    response_data = {
        'message': None,
    }
    book_id = request.POST['bid']  # get the book id from post data
    rating = request.POST['rating']
    rid = request.POST['rid']
    tmp = Review.objects.filter(book=book_id, reviewer=request.user)
    if len(tmp) == 0:
        Review.objects.create(
            book=Book.objects.get(id=book_id), reviewer=request.user, rating=rating)
    else:
        Review.objects.filter(
            book=book_id, reviewer=request.user).update(rating=rating)
    allr = Review.objects.filter(book=book_id)
    rt = 0
    for obj in allr:
        rt += obj.rating
    ru = len(allr)
    newr = rt/ru
    Book.objects.filter(id=book_id).update(
        rating=newr)
    BookCopy.objects.filter(id=rid).update(
        status=True, borrow_date=None, borrower=None)
    response_data['message'] = 1

    return JsonResponse(response_data)
