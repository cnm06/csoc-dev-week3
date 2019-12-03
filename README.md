# Library Management System 

This project is the Django backend of a library web application. 



# Features

* Book List View - Displays list of all the books available in the library.

* Book Detail View - Displays information such as genre, author, summary, price etc. of the book selected.

* Authentication - Views for login, logout and user registration.

* Issue a Book - Once logged in, user selects a book to issue. Systems confirms availability based on number of copies remaining                            unissued by any other user and displays whether or not the book can be issued.

* View Loaned Books - User checks his/her book-issue history and due date for returning the books.

* Returning an issued book - User enters book id as an argument and system marks the book-copy as returned. 

* Rating system - System allows the user to enter any integer between 0 to 10(both inclusive) to rate the book. Final rating would be the                     average of all user ratings.


