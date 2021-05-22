from django.urls import path, include
from book.api.create import CreateBook
from book.api.delete import DeleteBook
from book.api.list import ListBook
from book.api.addtocart import AddtoCart
from book.api.removefromcart import RemovefromCart

urlpatterns = [
    path('create/', CreateBook.as_view() , name = 'create book' ),
    path('<int:del_id>/delete/' , DeleteBook.as_view() , name = 'delete book'),
    path('' , ListBook.as_view() , name = 'list book'),
    path('<int:b_id>/add/', AddtoCart.as_view() , name ='add to cart'),
    path('<int:b_id>/removefromcart/', RemovefromCart.as_view() , name ='remove from cart'),

]
