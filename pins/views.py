from rest_framework import viewsets
from rest_framework import generics
from .models import Category, Pin, Board, SavedPin
from .serializers import (
    CategorySerializer, PinSerializer, BoardSerializer, SavedPinSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PinViewSet(viewsets.ModelViewSet):
    queryset = Pin.objects.all().order_by("-created_at")
    serializer_class = PinSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class SavedPinViewSet(viewsets.ModelViewSet):
    queryset = SavedPin.objects.all()
    serializer_class = SavedPinSerializer

class PinListCreateView(generics.ListCreateAPIView):
    serializer_class = PinSerializer

    # Fetch pins belonging only to the selected board slug (e.g., 'food')
    def get_queryset(self):
        board_slug = self.kwargs['board_slug']
        return Pin.objects.filter(board__slug=board_slug)

    # Automatically link the new Pin to the target Board
    def perform_create(self, serializer):
        board_slug = self.kwargs['board_slug']
        board = Board.objects.get(slug=board_slug)
        serializer.save(board=board)