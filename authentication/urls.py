from django.urls import path
from authentication.views import *

urlpatterns = [
    path('login/', loginView, name="login"),
    path('register/', registerView, name="register"),
    path('logout/', logoutView, name='logout'),
    path('loginlogic', loginlogicView, name="login-logic"),
    path('registerlogic', registerlogicView, name="register-logic"),
]
