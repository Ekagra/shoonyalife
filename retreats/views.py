from rest_framework import viewsets, filters, serializers
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Retreat, Booking
from .serializers import RetreatSerializer, BookingSerializer


class RetreatViewSet(viewsets.ModelViewSet):
    queryset = Retreat.objects.all()
    serializer_class = RetreatSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['location', 'price', 'duration']
    search_fields = ['title', 'description', 'location']
    pagination_class = PageNumberPagination


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def book(self, serializer):
        # Check if the user has already booked this retreat
        retreat_id = self.request.data.get('retreat')
        user_id = self.request.data.get('user_id')
        if Booking.objects.filter(retreat_id=retreat_id, user_id=user_id).exists():
            raise serializers.ValidationError("You have already booked this retreat.")
        serializer.save()
