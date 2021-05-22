from rest_framework.views import APIView
from user.api.decode import decode_jwt
from django.http import JsonResponse
from rest_framework import status
from book.models import Book

class DeleteBook(APIView):
    def post(self, request , del_id):
        user = decode_jwt(request)
        if(user.is_admin):
            try:
               book = Book.objects.get(id = del_id)
               book.delete() 
               return JsonResponse({
                   "message" : "delete success"
               } , status = status.HTTP_200_OK)
            except:
                return JsonResponse({
                    "message" : "not found book"
                } ,status = status.HTTP_404_NOT_FOUND)
        return JsonResponse({
            "message" : "token fail"
        } , status = status.HTTP_400_BAD_REQUEST)