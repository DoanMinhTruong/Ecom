from rest_framework.views import APIView
from book.serializers import BookSerializer
from user.api.decode import decode_jwt
from rest_framework import status
from django.http import JsonResponse

class CreateBook(APIView):
    def post(self, request):
        user = decode_jwt(request)
        if(user.is_admin):
            book = BookSerializer(data = request.data)
            if(book.is_valid()):
                book.save()
                return JsonResponse({
                    "message" : "create success"
                } , status = status.HTTP_200_OK)
            return JsonResponse({
                "message" : book.errors
            } , status = status.HTTP_400_BAD_REQUEST)        
        return JsonResponse({
                "message" : "token fail"
            } , status = status.HTTP_400_BAD_REQUEST)