from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import DogSerializer
from .models import Dog
from .permissions import IsUserOrReadOnly

class DogList(ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class DogDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsUserOrReadOnly,)
    queryset = Dog.objects.all()
    serializer_class = DogSerializer