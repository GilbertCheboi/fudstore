"""ecommerce URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView, RedirectView


from accounts.views import LoginView, RegisterView, GuestRegisterView
from addresses.views import (
    AddressCreateView,
    AddressListView,
    AddressUpdateView,
    checkout_address_create_view, 
    checkout_address_reuse_view
    )
from analytics.views import SalesView, SalesAjaxView
from billing.views import payment_method_view, payment_method_createview, get_quantity
from carts.views import cart_detail_api_view
from marketing.views import MarketingPreferenceUpdateView, MailchimpWebhookView
from orders.views import LibraryView
from products.views import CategoryList, HouseHold, FreshFood, Bakery, CupBoard, ProductListView, Fruits, Milk, Drinks, SoftDrinks, Meat, get_quantity
from .views import home_page, about_page, contact_page

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^about/$', about_page, name='about'),
    #url(r'^about/$', quantity_form, name='quantity_form'),
    #url(r'^accounts/login/$', RedirectView.as_view(url='/login')),
    url(r'^accounts/$', RedirectView.as_view(url='/account')),
    url(r'^account/', include("accounts.urls", namespace='account')),
    url(r'^accounts/', include("accounts.passwords.urls")),
    url(r'^address/$', RedirectView.as_view(url='/addresses')),
    url(r'^addresses/$', AddressListView.as_view(), name='addresses'),
    url(r'^addresses/create/$', AddressCreateView.as_view(), name='address-create'),
    url(r'^addresses/(?P<pk>\d+)/$', AddressUpdateView.as_view(), name='address-update'),
    url(r'^analytics/sales/$', SalesView.as_view(), name='sales-analytics'),
    url(r'^analytics/sales/data/$', SalesAjaxView.as_view(), name='sales-analytics-data'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name='checkout_address_reuse'),
    url(r'^register/guest/$', GuestRegisterView.as_view(), name='guest_register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/cart/$', cart_detail_api_view, name='api-cart'),
    url(r'^cart/', include("carts.urls", namespace='cart')),
    url(r'^billing/payment-method/$', payment_method_view, name='billing-payment-method'),
    url(r'^billing/quantity_form/$', get_quantity, name='quan'),
    url(r'^products/quantity_form/$', get_quantity, name='update-cart'),
    url(r'^billing/payment-method/create/$', payment_method_createview, name='billing-payment-method-endpoint'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
    url(r'^library/$', LibraryView.as_view(), name='library'),
    url(r'^household/$', HouseHold.as_view(), name='house_hold'),
    url(r'^cupboard/$', CupBoard.as_view(), name='cup_board'),
    url(r'^fruits/$', Fruits.as_view(), name='fruits'),
    url(r'^milk/$', Milk.as_view(), name='milk'),
    url(r'^meat/$', Meat.as_view(), name='meat'),
    url(r'^drinks/$', Drinks.as_view(), name='drinks'),
    url(r'^softdrinks/$', SoftDrinks.as_view(), name='soft_drinks'),
    url(r'^freshfood/$', FreshFood.as_view(), name='fresh_food'),
    url(r'^bakery/$', Bakery.as_view(), name='bakery'),
    url(r'^category/$', CategoryList.as_view(), name='category_list'),
    url(r'^orders/', include("orders.urls", namespace='orders')),
    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^search/', include("search.urls", namespace='search')),
    url(r'^settings/$', RedirectView.as_view(url='/account')),
    url(r'^settings/email/$', MarketingPreferenceUpdateView.as_view(), name='marketing-pref'),
    url(r'^webhooks/mailchimp/$', MailchimpWebhookView.as_view(), name='webhooks-mailchimp'),
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
