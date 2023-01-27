from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import generics
import requests 
from .serializer import Registration, GETCollections, POSTCollections
from .serializer import GETCollection, PUTCollection, RequestCountSerializer
# Create your views here.
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny
#from rest_framework_simplejwt import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Collections
from .middleware import CountRequestsMiddleware
'''
@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def movie_list(request):
    r_data = requests.get('https://demo.credy.in/api/v1/maya/movies/')
    while(r_data.status_code != 200):
        r_data = requests.get('https://demo.credy.in/api/v1/maya/movies/')
    #result_json = json.loads(r_data.text)
    return Response(r_data.json())
'''

class MovieList(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        r_data = requests.get('https://demo.credy.in/api/v1/maya/movies')
        while(r_data.status_code != 200):
           r_data = requests.get('https://demo.credy.in/api/v1/maya/movies')
        return Response(r_data.json())
       # else:
        #    return Response({'details: The user has not been authenticated.'}) 

class Register(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = Registration
    def post(self,request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user is not None:
            #login(request, user)
            access_token = str(RefreshToken.for_user(user).access_token)
            return Response({
                'access_token' : access_token,
            })

class CollectionsView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GETCollections 
        elif self.request.method == 'POST':
            return POSTCollections 
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        collection = serializer.save(user = request.user)
        return Response({'collection_uuid' : collection.uuid})
    
    def get(self, request, *args, **kwargs):
        collection = Collections.objects.filter(user = request.user)
        if collection.exists():
            serializer = self.get_serializer()
            response = serializer.get_collection(collection)
            return response
        else:
            return Response({'error' : 'There are no collections under the current user.'})

class CollectionView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GETCollection
        elif self.request.method == 'PUT':
            return PUTCollection
    def put(self, request, uuid, *args, **kwargs):
        collection = Collections.objects.filter(uuid=uuid, user=request.user)
        if collection.exists():
            first_val = collection[0]
            serializer = self.get_serializer(first_val, data = request.data, partial = True)
            serializer.is_valid(raise_exception = True)
            response = serializer.save()
            return response
        else:
            return Response({'error':'The requested unique id does not exist in the database'})
    
    def get(self, request, uuid, *args, **kwargs):
        collection = Collections.objects.filter(uuid = uuid, user = request.user)
        if collection.exists():
            first_val = collection[0]
            serializer  = self.get_serializer()
            response = serializer.get_collection(first_val)
            return response
        else:
            return Response({'error':'The requested unique id does not exist in the database'})
    
    def delete(self, request, uuid, *args, **kwargs):
        collection = Collections.objects.filter(uuid = uuid, user = request.user)
        if collection.exists():
            first_val = collection[0]
            first_val.delete()
            return Response({'is_success':True})
        else:
            return Response({'error': 'The requested unique id does not exist in the database'})
    

class RequestCountView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        #count_obj = CountRequestsMiddleware(None)
        count = request.request_counter
        #serializer = RequestCountSerializer({'requests':count})
        return Response({'requests':count})

class RequestCountResetView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        count_obj = CountRequestsMiddleware(None)
        count_obj.reset_count()
        return Response({'message':'request count reset successfully'})

        

