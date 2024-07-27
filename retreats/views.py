from rest_framework import viewsets, filters, serializers, status
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            retreat_id = request.data.get('retreat')
            user_id = request.data.get('user_id')

            # Check if the user has already booked this retreat
            if Booking.objects.filter(retreat_id=retreat_id, user_id=user_id).exists():
                return Response(
                    {
                        'error': 'You have already booked this retreat.',
                        'details': {
                            'retreat_id': retreat_id,
                            'user_id': user_id
                        }
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Proceed to save the booking if no duplicate
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {
                    'status': 'Booking created successfully',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        except ValidationError as e:
            return Response(
                {
                    'error': 'Invalid data',
                    'details': e.detail
                },
                status=status.HTTP_400_BAD_REQUEST
            )