from django.urls import path

from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    # PasswordResetView,
    # PasswordResetConfirmView,
)

from rest_framework_simplejwt.views import TokenVerifyView

from . import views

urlpatterns = [
    path("list/", views.user_list, name="user_list"),
    path("reg/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
    # Этот функционал нужно доработать подключить email-порты
    # Сброс пароля реализуется отправлением письма на email.
    # path("pass-reset/", PasswordResetView.as_view()),
    # path(
    #     "pass-reset-conf/<uidb64>/<token>/",
    #     PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
]
