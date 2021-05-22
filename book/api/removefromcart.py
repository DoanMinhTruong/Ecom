from rest_framework.views import APIView
from user.api.decode import decode_jwt
from cart.models import Cart
from rest_framework import status
from django.http import JsonResponse

class RemovefromCart(APIView):
    def post(self, request, b_id):
        user = decode_jwt(request)
        try:
            cart = Cart.objects.get(book_id = b_id , user_id = user.id)
            cart.delete()
            return JsonResponse({
                "message" : "Delete success"
            }  ,status = status.HTTP_200_OK)
        except:
            return JsonResponse({
                "message": "Fail"
            } , status = status.HTTP_400_BAD_REQUEST)