from django.shortcuts import render
#from django.http import HttpResponse
from .models import Sale
from .utils import get_plot

# Create your views here.
def home(request):
    qs = Sale.objects.all()
    x = [x.item for x in qs]
    y = [y.price for y in qs]
    chart = get_plot(x, y)
    return render(request, "home.html", {"chart": chart})