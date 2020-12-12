from rest_framework import status
from rest_framework.response import Response

from .models import booking
from .serializers import BookingSerializer
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView


class CreateBookingAPIView(CreateAPIView):
    serializer_class = BookingSerializer

    def post(self, request, *args, **kwargs):
        print("REQUEST DATA", request.data)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
class BookingListView(ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        return booking.objects.filter()

    def post(self, request,  *args, **kwargs):
        data = list()
        get_status = request.data["status"]
        booking_data = booking.objects.filter(status=get_status)
        serializer = self.get_serializer(booking_data, many=True)


        for booking in serializer.data:
            data.append({
                "id": booking[0]["id"],
                "user_id": booking[0]["user_id"],
                "package_id": booking[0]["package_id"],
                "fromdate": booking[0]["fromdate"],
                "todate": booking[0]["todate"]
            })
        return Response(data, status.HTTP_200_OK)


class DeleteBookingView(DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        booking_id = self.kwargs["pk"]
        booking.objects.filter(id=booking_id).delete()
        return Response(status.HTTP_204_NO_CONTENT)
