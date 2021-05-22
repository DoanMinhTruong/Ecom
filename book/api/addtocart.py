from rest_framework.views import APIView
from user.api.decode import decode_jwt
from cart.serializers import CartSerializer
from rest_framework import status
from django.http import JsonResponse

class AddtoCart(APIView):
    def post(self, request, b_id):
        user = decode_jwt(request)
        try:
            datum = {}
            datum['user'] = user.id
            datum['book'] = b_id
            cart = CartSerializer(data = datum)
            if(cart.is_valid()):
                cart.save()
                return JsonResponse({
                    "message" : "add success"
                } ,status = status.HTTP_200_OK)
            return JsonResponse({
                "message" : "invalid data"
            }, status = status.HTTP_400_BAD_REQUEST)
        except:
            return JsonResponse({
                "message" : "fail"
            }, status = status.HTTP_400_BAD_REQUEST)
        
        # datum = {}
        # datum['user'] = user.id
        # datum['book'] = b_id
        # cart = CartSerializer(data = datum)
        # if(cart.is_valid()):
        #     cart.save()
        #     return JsonResponse({
        #             "message" : "add success"
        #         } ,status = status.HTTP_200_OK)
        # return JsonResponse({
        #         "message" : "invalid data"
        #     }, status = status.HTTP_400_BAD_REQUEST)
            