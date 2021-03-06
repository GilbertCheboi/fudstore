# from django.views import ListView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, View, TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render, get_object_or_404, redirect

from analytics.mixins import ObjectViewedMixin, CartAddProductForm

from carts.models import Cart
#from .forms import CartAddProductForm

from .models import Product, Category, ProductFile, SubCategory


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()



class ProductFeaturedDetailView(ObjectViewedMixin, DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


class UserProductHistoryView(LoginRequiredMixin, ListView):
    template_name = "products/user-history.html"
    def get_context_data(self, *args, **kwargs):
        context = super(UserProductHistoryView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        views = request.user.objectviewed_set.by_model(Product, model_queryset=False)
        return views



class CategoryList(ListView):
    model = Category

class Vegetables(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(category__name='Vegetables')
    template_name = "products/vegetables.html"


class TomatoesOnions(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(category__name='TomatoesOnions')
    template_name = "products/tomatoesonions.html"

class PotatoesRoots(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(category__name='PotatoesRoots')
    template_name = "products/potatoesroots.html"

class CupBoard(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(category__name='CupBoard')
    template_name = "products/cup_board.html"

class Fruits(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(category__name='Fruits')
    template_name = "products/fruits.html"

class Milk(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(category__name='Milk')
    template_name = "products/milk.html"

class Meat(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(category__name='Meat')
    template_name = "products/meat.html"

class Drinks(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(category__name='Drinks')
    template_name = "products/drinks.html"

class SoftDrinks(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(category__name='SoftDrinks')
    template_name = "products/soft_drinks.html"


class SubCategoryList(ListView):

    model = SubCategory
#vegetables
class Spinach(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Spinach')
    template_name = "products/spinach.html"

class Cabbage(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Cabbage')
    template_name = "products/cabbage.html"

class Managu(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Managu')
    template_name = "products/managu.html"
class Pumpkin(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Pumpkin')
    template_name = "products/pumpkin.html"
class PumpkinLeaves(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='PumkinLeaves')
    template_name = "products/pumpkinleaves.html"

class Peas(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Peas')
    template_name = "products/peas.html"

class Beans(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Beans')
    template_name = "products/beans.html"

class Lettuce(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Lettuce')
    template_name = "products/lettuce.html"


class Brocolli(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Brocolli')
    template_name = "products/brocolli.html"

class Mushroom(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Mushroom')
    template_name = "products/mushroom.html"

class Butternut(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Butternut')
    template_name = "products/butternut.html"

class Beetroot(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Beetroot')
    template_name = "products/beetroot.html"
class Maize(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Maize')
    template_name = "products/maize.html"



class Kales(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Kales')
    template_name = "products/kales.html"


class Cucumber(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Cucumber')
    template_name = "products/cucumber.html"
# Fruits
class Watermelon(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Watermelon')
    template_name = "products/watermelon.html"


class Bananas(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Bananas')
    template_name = "products/bananas.html"


class Mango(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Mango')
    template_name = "products/mango.html"

class Oranges(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Oranges')
    template_name = "products/oranges.html"
class Apples(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Apples')
    template_name = "products/apples.html"
class Strawberry(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Strawberry')
    template_name = "products/strawberry.html"
class Avocado(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Avocado')
    template_name = "products/avocado.html"
class Lemon(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Lemon')
    template_name = "products/lemon.html"

class Guava(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Guava')
    template_name = "products/guava.html"

class Grape(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Grape')
    template_name = "products/grape.html"

class Pineapples(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Pineapples')
    template_name = "products/pineapples.html"

class Pear(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Pear')
    template_name = "products/pear.html"

class Passion(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Passion')
    template_name = "products/passion.html"

class Tomatoes(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Tomatoes')
    template_name = "products/tomatoes.html"

class GreenOnions(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='GreenOnioins')
    template_name = "products/greenonions.html"

class RedOnions(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='RedOnions')
    template_name = "products/redonions.html"

class YellowOnions(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='YellowOnions')
    template_name = "products/yellowonions.html"



class Garlic(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Garlic')
    template_name = "products/garlic.html"

class PilipiliHoho(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='PilipiliHoho')
    template_name = "products/pilipilihoho.html"

class DaikonRadish(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='DaikonRadish')
    template_name = "products/daikonradish.html"

class Leeks(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Leeks')
    template_name = "products/leeks.html"


class Zuchini(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Zuchini')
    template_name = "products/zuchini.html"



class LeafyOnions(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='LeafOnions')
    template_name = "products/leafonions.html"



class Jicama(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Jiacama')
    template_name = "products/jicama.html"



class Dhania(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Dhania')
    template_name = "products/dhania.html"



class GreenRedChilli(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='GreenRedChilli')
    template_name = "products/greenredchilli.html"

class Potatoes(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Potatoes')
    template_name = "products/potatoes.html"

class SweetPotatoes(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='SweetPotatoes')
    template_name = "products/sweetpotatoes.html"


class Carrots(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Carrots')
    template_name = "products/carrots.html"



class Cassava(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Cassava')
    template_name = "products/cassava.html"


#Milk
class PasturisedMilk(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='PasturisedMilk')
    template_name = "products/pasturisedmilk.html"



class NonPasturisedMilk(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='NonPasturisedMilk')
    template_name = "products/nonpasturisedmilk.html"



class Mursik(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Mursik')
    template_name = "products/mursik.html"
class Garlic(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Garlic')
    template_name = "products/garlic.html"

class Garlic(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Garlic')
    template_name = "products/garlic.html"



class Garlic(ListView):

    context_object_name = 'product_list'
    queryset = Product.objects.filter(subcategory__name='Garlic')
    template_name = "products/garlic.html"

def get_quantity(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CartAddProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CartAddProductForm()

    return render(request, 'products/snippets/update-cart.html', {'form': form})
    


class ProductListView(ListView):
    template_name = "products/list.html"
    

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()




def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)







class ProductDetailSlugView( ObjectViewedMixin, CartAddProductForm, DetailView ):
    queryset = Product.objects.all()
    #quantity_form = CartAddProductForm
    
    template_name = "products/detail.html"


    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        #instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance
    

    
import os
from wsgiref.util import FileWrapper # this used in django
from mimetypes import guess_type

from django.conf import settings
from orders.models import ProductPurchase

class ProductDownloadView(View):
    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        pk = kwargs.get('pk')
        downloads_qs = ProductFile.objects.filter(pk=pk, product__slug=slug)
        if downloads_qs.count() != 1:
            raise Http404("Download not found")
        download_obj = downloads_qs.first()
        # permission checks
        
        can_download = False
        user_ready  = True
        if download_obj.user_required:
            if not request.user.is_authenticated():
                user_ready = False

        purchased_products = Product.objects.none()
        if download_obj.free:
            can_download = True
            user_ready = True
        else:
            # not free
            purchased_products = ProductPurchase.objects.products_by_request(request)
            if download_obj.product in purchased_products:
                can_download = True
        if not can_download or not user_ready:
            messages.error(request, "You do not have access to download this item")
            return redirect(download_obj.get_default_url())

        aws_filepath = download_obj.generate_download_url()
        print(aws_filepath)
        return HttpResponseRedirect(aws_filepath)
        # file_root = settings.PROTECTED_ROOT
        # filepath = download_obj.file.path # .url /media/
        # final_filepath = os.path.join(file_root, filepath) # where the file is stored
        # with open(final_filepath, 'rb') as f:
        #     wrapper = FileWrapper(f)
        #     mimetype = 'application/force-download'
        #     gussed_mimetype = guess_type(filepath)[0] # filename.mp4
        #     if gussed_mimetype:
        #         mimetype = gussed_mimetype
        #     response = HttpResponse(wrapper, content_type=mimetype)
        #     response['Content-Disposition'] = "attachment;filename=%s" %(download_obj.name)
        #     response["X-SendFile"] = str(download_obj.name)
        #     return response
        #return redirect(download_obj.get_default_url())




class ProductDetailView(ObjectViewedMixin, DetailView):
    
    #queryset = Product.objects.all()
    template_name = "products/detail.html"
    #quantity_form = CartAddProductForm

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        # context['abc'] = 123
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")

        context = {
        'object': instance
    }
        return context

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)


def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk, featured=True) #id
    # instance = get_object_or_404(Product, pk=pk, featured=True)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesn't exist")
    # except:
    #     print("huh?")

    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesn't exist")
    #print(instance)
    # qs  = Product.objects.filter(id=pk)

    # #print(qs)
    # if qs.exists() and qs.count() == 1: # len(qs)
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")

    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)







