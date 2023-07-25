from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .models import Product
from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.aggregates import StringAgg, ArrayAgg
import logging

logger = logging.getLogger("mylogger")



Message = {"status": "", "message": ""}

# Create your views here.
class ProductListView(APIView):
    
    def get(self, request):
        # product = Product.objects.all().values('name');
        # product = Product.objects.annotate(search=SearchVector("name") + SearchVector("overlay__discipline"))\
        #     .filter(search='automation').values()
        result = []
        # result = list(Product.objects.annotate(total_names = ArrayAgg("name", delimiter=', ', distinct=True)).values('name').order_by('name'))
        result = Product.objects.name_list()
        # for product in Product.objects.all():
        #     logger.info("La query: " + str(Product.objects.all().query))
        #     result.append(product.name)
        Message['status'] = str(status.HTTP_200_OK)
        Message['message'] = result
        # return Response(response_data, status=status.HTTP_200_OK)
        return JsonResponse(Message, content_type="application/json");


class AuthToken(ObtainAuthToken):
    
    def get(self, request):
        """
        Returns authenticated user API token
        """
        if request.user.is_anonymous:
            Error = {
                'status': status.HTTP_401_UNAUTHORIZED,
                'message': 'Unauthorized call'}
            return Response(Error, status=status.HTTP_401_UNAUTHORIZED)
        user = request.user

        token, created = Token.objects.get_or_create(user=user)
        return Response({'api-token': token.key})
    
    def put(self, request):
        """
        Rotates authenticated user API token
        """
        if request.user.is_anonymous:
            Error = {
                'status': status.HTTP_401_UNAUTHORIZED,
                'message': 'Unauthorized call'}
            return Response(Error, status=status.HTTP_401_UNAUTHORIZED)
        
        user = request.user

        token = Token.objects.get(user=user)
        token.delete()
        token = Token.objects.create(user=user)

        return Response({'api-token': token.key}, status=status.HTTP_201_CREATED)