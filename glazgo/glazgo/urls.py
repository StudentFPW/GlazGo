"""
URL configuration for glazgo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from ats.views import *

router = routers.DefaultRouter()
router.register(r"cph", CPHistoryViewSet)
router.register(r"resp", ResponsibilitiesViewSet)
router.register(r"req", RequirementsViewSet)
router.register(r"vac", VacancyViewSet)
router.register(r"cand", CandidateViewSet)
router.register(r"c-p", CPromotionViewSet)
# router.register(r"mes", MessageViewSet)
router.register(r"w-cand", WaitingCandidateViewSet)
router.register(r"new-cand", CandidateAddedViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="GlazGo API",
        default_version="v1",
        description="GlazGo API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("api-", include(router.urls)),
    path("secret-k6F8-admin-73rbHG/", admin.site.urls),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/reg/", include("dj_rest_auth.registration.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path("chat/", include("chat.urls")),
    path("users/", include("users.urls")),
    path("swag<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(
        "swag/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]