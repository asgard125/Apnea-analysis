from django.urls import path, include
from api import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
  
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("predict/", views.predict),
    path('api/', include('api.urls')),
    path('upload-file/', views.FileUploadAPIView.as_view(), name='upload-file'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

