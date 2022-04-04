from django.contrib.auth.hashers import check_password

from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .serializers import *

from .models import *


class AdminRegistrationApi(generics.GenericAPIView):
    serializer_class = AdminRegistrationSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({
                'message': 'Successful',
                'Result': AdminRegistrationSerializer(user).data,
                'HasError': False,
                'status': 200
            })
        except Exception as e:
            return Response({
                'message': 'Fail',
                'Result': [],
                'HasError': True,
                'status': 400
            })


class AdminLoginApi(generics.GenericAPIView):
    serializer_class = AdminLoginSerializer

    def post(self, request):
        username = request.data.get('Username')
        password = request.data.get('Password')
        if AdminTable.objects.filter(Email=username).first():
            user = AdminTable.objects.filter(Email=username).first()
            if check_password(password, user.Password):
                s = AdminLoginSerializer(user, data=request.data, partial=True)
                s.is_valid(raise_exception=True)
                s.save()
                serializer_class = AdminRegistrationSerializer(user).data
                return Response({
                    'message': 'Successful',
                    'Result': serializer_class.data,
                    'HasError': False,
                    'status': 200
                })
            else:
                return Response({
                    'message': 'user not found',
                    'Result': [],
                    'HasError': True,
                    'status': 400
                })

        return Response({
            'message': 'Please enter valid details',
            'Result': [],
            'HasError': True,
            'status': 400
        })


class BooksEntryApi(generics.GenericAPIView):
    serializer_class = BooksEntrySerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({
                'message': 'Successful',
                'Result': BooksEntrySerializer(user).data,
                'HasError': False,
                'status': 200
            })
        except Exception as e:
            return Response({
                'message': 'Fail',
                'Result': [],
                'HasError': True,
                'status': 400
            })


class GetEnterdBooks(generics.GenericAPIView):
    serializer_class = BooksEntrySerializer
    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            queryset = BooksTable.objects.all()
            serializer_class = BooksEntrySerializer(queryset, many=True)
            return Response({
                'message': 'Successful',
                'Result': serializer_class.data,
                'HasError': False,
                'status': 200
            })
        except Exception as e:
            return Response({
                'message': 'Fail',
                'Result': [],
                'HasError': True,
                'status': 400
            })


class BooksUpdate(generics.GenericAPIView):
    serializer_class = BooksEntrySerializer

    def put(self, request, id):
        try:
            r = BooksTable.objects.get(id=id)

            s = BooksEntrySerializer(r, data=request.data)
            s.is_valid(raise_exception=True)
            s.save()

            return Response({
                'message': 'Successful',

                'HasError': False,
                'status': 200
            })
        except BooksTable.DoesNotExist as e:

            return Response({
                'message': 'Fail',
                'HasError': True,
                'status': 400
            })


class DeleteBook(generics.GenericAPIView):
    serializer_class = BooksEntrySerializer

    def delete(self, request, id, format=None):
        try:
            d = BooksTable.objects.get(id=id)
            d.delete()

            return Response({
                'message': 'Successful',
                'HasError': False,
                'status': 200
            })
        except BooksTable.DoesNotExist as e:

            return Response({
                'message': 'Fail',
                'HasError': True,
                'status': 400
            })
