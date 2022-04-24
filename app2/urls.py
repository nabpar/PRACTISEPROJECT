
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from app2 import views


# this is for swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('',include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/topic/listview/',views.GetTopic.as_view()),
    path('api/topic/create/',views.CreateTopic.as_view()),
    path('api/topic/update/',views.UpdateTopic.as_view()),
    path('api/topic/delste',views.DeleteTopic.as_view()),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
