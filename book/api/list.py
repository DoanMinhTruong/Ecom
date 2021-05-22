from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from book.models import Book

class ListBook(APIView):
    def get(self, request):
        try:
            return JsonResponse(list(Book.objects.all().values()), safe=False)
        except:
            return JsonResponse({
                "message" : "0 book"
            } , status = status.HTTP_204_NO_CONTENT)