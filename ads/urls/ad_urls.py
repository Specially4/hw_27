from django.urls import path

from ads.views import (AdCreateView, AdDeleteView, AdListView, AdRetrieveView,
                       AdUpdateView, AdUploadImageView)

urlpatterns = [
    path('', AdListView.as_view()),
    path('<int:pk>/', AdRetrieveView.as_view()),
    path('create/', AdCreateView.as_view()),
    path('<int:pk>/upload_image/', AdUploadImageView.as_view()),
    path('<int:pk>/update/', AdUpdateView.as_view()),
    path('<int:pk>/delete/', AdDeleteView.as_view()),
]
