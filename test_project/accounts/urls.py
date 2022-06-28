from django.urls import path
from .views import RegistrerFormUser, LoginFormView, LogoutView

urlpatterns = [
    path('register/', RegistrerFormUser.as_view(), name="register"),
    path('login/', LoginFormView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
