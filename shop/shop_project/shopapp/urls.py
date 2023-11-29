
from django.urls import path

from shopapp import views
app_name='shopapp'
urlpatterns = [

    path('',views.allprocat,name='allprocat'),
    path('<slug:c_slug>/',views.allprocat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodet,name='product_category_detail')
]