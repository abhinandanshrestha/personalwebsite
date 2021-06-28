from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',views.index, name="index"),
  path('blogs/', views.PostList.as_view(), name="blog"),
  path('<slug:slug>/', views.DetailView.as_view(), name="post_detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)