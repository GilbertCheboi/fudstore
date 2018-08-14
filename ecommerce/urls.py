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
from products.views import  (
    CategoryList, Spinach,
    TomatoesOnions, PotatoesRoots,
    CupBoard, ProductListView,
    Fruits, Milk,
    Drinks, SoftDrinks,
    Meat, get_quantity,
    Cabbage,
        Pumpkin,
        Managu,
        PumpkinLeaves,
        Peas,
        Lettuce,
        Brocolli,
        Mushroom,
        Butternut,
        Beetroot,
        Beans,
        Maize,
        Kales,
        Cucumber,
        Watermelon,
        Bananas,
        Mango,
        Oranges,
        Apples,
        Strawberry,
        Avocado,
        Lemon,
        Guava,
        Grape,
        Pineapples,
        Pear,
        Passion,
        Tomatoes,
        GreenOnions,
        YellowOnions,
        RedOnions,
        Garlic,
        PilipiliHoho,
        DaikonRadish,
        Leeks,
        Zuchini,
        LeafyOnions,
        Jicama,
        Dhania,
        GreenRedChilli,
        Potatoes,
        SweetPotatoes,
        Carrots,
        Cassava,
        PasturisedMilk,
        NonPasturisedMilk,
        Mursik,
        Vegetables

    )
from .views import home_page, about_page, contact_page

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^about/$', about_page, name='about'),
    url(r'^accounts/login/$', RedirectView.as_view(url='/login')),
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
    url(r'^cupboard/$', CupBoard.as_view(), name='cup_board'),
    url(r'^fruits/$', Fruits.as_view(), name='fruits'),
    url(r'^milk/$', Milk.as_view(), name='milk'),
    url(r'^potatoesroots/$', PotatoesRoots.as_view(), name='potatoesroots'),
    url(r'^meat/$', Meat.as_view(), name='meat'),
    url(r'^drinks/$', Drinks.as_view(), name='drinks'),
    url(r'^spinach/$', Spinach.as_view(), name='spinach'),
    url(r'^cabbage/$', Cabbage.as_view(), name='cabbage'),
    url(r'^managu/$', Managu.as_view(), name='managu'),
    url(r'^vegetables/$', Vegetables.as_view(), name='vegetables'),
    url(r'^pumpkin/$', Pumpkin.as_view(), name='pumpkin'),
    url(r'^pumpkinLeavesu/$', PumpkinLeaves.as_view(), name='pumpkinleaves'),
    url(r'^peas/$', Peas.as_view(), name='peas'),
    url(r'^lettuce/$', Lettuce.as_view(), name='lettuce'),
    url(r'^brocolli/$', Brocolli.as_view(), name='brocolli'),
    url(r'^mushroom/$', Mushroom.as_view(), name='mushroom'),
    url(r'^butternut/$', Butternut.as_view(), name='butternut'),
    url(r'^beetroot/$', Beetroot.as_view(), name='beetroot'),
    url(r'^beans/$', Beans.as_view(), name='beans'),
    url(r'^maize/$', Maize.as_view(), name='maize'),
    url(r'^kales/$', Kales.as_view(), name='kales'),
    url(r'^cucumber/$', Cucumber.as_view(), name='cucumber'),
    url(r'^watermelon/$', Watermelon.as_view(), name='watermelon'),
    url(r'^bananas/$', Bananas.as_view(), name='bananas'),
    url(r'^mango/$', Mango.as_view(), name='mango'),
    url(r'^oranges/$', Oranges.as_view(), name='oranges'),
    url(r'^apples/$', Apples.as_view(), name='apples'),
    url(r'^strawberry/$', Strawberry.as_view(), name='strawberry'),
    url(r'^avocado/$', Avocado.as_view(), name='avocado'),
    url(r'^lemon/$', Lemon.as_view(), name='lemon'),
    url(r'^guava/$', Guava.as_view(), name='guava'),
    url(r'^grape/$', Grape.as_view(), name='grape'),
    url(r'^tomatoesonions/$', TomatoesOnions.as_view(), name='tomatoesonions'),
    url(r'^pineapples/$', Pineapples.as_view(), name='pineapples'),
    url(r'^pear/$', Pear.as_view(), name='pear'),
    url(r'^passion/$', Passion.as_view(), name='passion'),
    url(r'^tomatoes/$', Tomatoes.as_view(), name='tomatoes'),
    url(r'^greenonions/$', GreenOnions.as_view(), name='greenonions'),
    url(r'^redonions/$', RedOnions.as_view(), name='redonions'),
    url(r'^yellowonions/$', YellowOnions.as_view(), name='yellowonions'),
    url(r'^garlic/$', Garlic.as_view(), name='garlic'),
    url(r'^pilipilihoho/$', PilipiliHoho.as_view(), name='pilipilihoho'),
    url(r'^daikonradish/$', DaikonRadish.as_view(), name='daikonradish'),
    url(r'^leeks/$', Leeks.as_view(), name='leeks'),
    url(r'^zuchini/$', Zuchini.as_view(), name='zuchini'),
    url(r'^leafyonions/$', LeafyOnions.as_view(), name='leafyonions'),
    url(r'^jicama/$', Jicama.as_view(), name='jicama'),
    url(r'^dhania/$', Dhania.as_view(), name='dhania'),
    url(r'^greenredchilli/$', GreenRedChilli.as_view(), name='greenredchilli'),
    url(r'^potatoes/$', Potatoes.as_view(), name='potatoes'),
    url(r'^sweetpotatoes/$', SweetPotatoes.as_view(), name='sweetpotatoes'),
    url(r'^carrots/$', Carrots.as_view(), name='carrots'),
    url(r'^cassava/$', Cassava.as_view(), name='cassava'),
    url(r'^pasturisedmilk/$', PasturisedMilk.as_view(), name='pasturisedmilk'),
    url(r'^nonpasturisedmilk/$', NonPasturisedMilk.as_view(), name='nonpasturisedmilk'),
    url(r'^mursik/$', Mursik.as_view(), name='mursik'),


    
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
