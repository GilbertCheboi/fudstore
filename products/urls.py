from django.conf.urls import url

from .views import (
        ProductListView, 
        ProductDetailSlugView, 
        ProductDownloadView,
        HouseHold,
        FreshFood,
        Bakery,
        CupBoard,
        Fruits,
        Milk,
        Meat,
        Drinks,
        SoftDrinks,
        CategoryList
        
        
        )

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/(?P<pk>\d+)/$', ProductDownloadView.as_view(), name='download'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<pk>\d+)/$',  HouseHold.as_view(), name='house_hold'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<pk>\d+)/$',  FreshFood.as_view(), name='fresh_food'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<pk>\d+)/$',  CupBoard.as_view(), name='cup_board'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<pk>\d+)/$',  Bakery.as_view(), name='bakery'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<pk>\d+)/$',  Fruits.as_view(), name='fruits'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<pk>\d+)/$',  Milk.as_view(), name='milk'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<pk>\d+)/$',  Meat.as_view(), name='meat'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<pk>\d+)/$',  Drinks.as_view(), name='drinks'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<pk>\d+)/$',  SoftDrinks.as_view(), name='soft_drinks'),
    url(r'^(?P<slug>[\w-]+)/(?P<pk>\d+)/$', CategoryList.as_view(), name='category_list')
]
