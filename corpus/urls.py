from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'corpus'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/tagging/', views.TaggingView.as_view(), name='tagging'),
    path('<int:pk>/tagging/update/', views.update)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
