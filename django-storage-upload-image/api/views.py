from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Image
from .serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

@api_view(['GET'])
def api_root(request):
    return Response({
        'message': 'Welcome to our Django REST Framework API',
        'status': 'API is working correctly',
        'endpoints': {
            'images': request.build_absolute_uri('/api/images/'),
        }
    })
