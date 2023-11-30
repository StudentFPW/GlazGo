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
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from ats.views import *
from referral_system.views import *
from users.views import *

router = routers.DefaultRouter()
router.register(r"cph", CPHistoryViewSet, basename="CPH")
router.register(r"vac", VacancyViewSet, basename="V")
router.register(r"cand", CandidateViewSet, basename="C")
router.register(r"c-p", CPromotionViewSet, basename="CP")
router.register(r"ref", RRViewSet, basename="RR")
router.register(r"refl", RCViewSet, basename="RC")
router.register(r"ud", UserViewSet, basename="UD")
router.register(r"cb", CandidateBaseViewSet, basename="CB")
router.register(r"re", RegionViewSet, basename="R")
router.register(r"wt", WorkTimeViewSet, basename="WT")
router.register(r"rfo", RFOViewSet, basename="RFO")
router.register(r"new-cand", CandidateAddedViewSet, basename="NC")
router.register(r"team", TeamViewSet, basename="T")

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
    path("chat/", include("chat.urls")),
    path("user/", include("users.urls")),
    path("teams/get_my_team/", get_my_team, name="get_my_team"),
    path("teams/add_member/", add_member, name="add_member"),
    path("swag<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(
        "swag/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
