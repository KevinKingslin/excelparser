from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

from .models import Product, Variations

# Create your views here.
def index(request):
    products = Product.objects.all()
    variations = Variations.objects.all()

    return render(request, "excelparser/index.html", {
        "products": products,
        "variations": variations,
        "productsCount": len(products),
        "variationsCount": len(variations)
    })