from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.authentication.serializers import (RegisterSerializer,
                                             SendCodeSerializer,
                                             VerifyCodeSerializer)


class SendCodeAPIView(GenericAPIView):
    """
    This view is send verification code to the phone number.
    """
    queryset = []
    permission_classes = ()
    authentication_classes = ()

    serializer_class = SendCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         context={'request': request,})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=200)
    

class VerifyCodeAPIView(GenericAPIView):
    """
    This view is check verify code 
    """
    queryset = []
    permission_classes = ()
    authentication_classes = ()

    serializer_class = VerifyCodeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)
    

class RegisterAPIView(GenericAPIView):
    """
    This view is register a new user.
    """
    queryset = []
    permission_classes = ()
    authentication_classes = ()

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)