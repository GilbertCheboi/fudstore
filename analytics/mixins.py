from .signals import object_viewed_signal
from .forms import CartAddProductForm
from django.views.generic.edit import FormView


class ObjectViewedMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(ObjectViewedMixin, self).get_context_data(*args, **kwargs)
        request = self.request
        instance  = context.get('object')
        if instance:
            object_viewed_signal.send(instance.__class__, instance=instance, request=request)
        return context



class CartAddProductForm(FormView):


    def get_context_data(self, *args, **kwargs):
        context = super(CartAddProductForm, self).get_context_data(*args, **kwargs)
        
        return context
    form_class = CartAddProductForm
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.CartAddProductForm()
        return super().form_valid(form)
