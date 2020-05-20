from django.urls import path

from .views import FileView

app_name = "file_upload_app"

urlpatterns = [
    path('upload_file/', FileView.as_view()),
]
