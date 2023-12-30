from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema
from events.serializers import EventSerializer


class EventView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=EventSerializer)
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            event = serializer.save()
            data = EventSerializer(event).data
            data.update(id=event.id)
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
