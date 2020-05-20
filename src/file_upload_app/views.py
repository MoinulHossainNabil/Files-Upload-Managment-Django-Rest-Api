import os

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import FileSerilizer


def upload_handler(up_file, uploader):
    for f in up_file:
        dest = f'uploaded_files/{uploader}'
        if not os.path.exists(dest):
            os.makedirs(dest)
        default_storage.save(f'{dest}/{f}', ContentFile(f.read()))


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        uploaded_files = request.FILES.getlist('file_name')
        uploader = dict(request.data)['uploader'][0]
        upload_handler(uploaded_files, uploader)
        file_serializer = FileSerilizer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
