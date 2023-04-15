from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
import openpyxl

from .models import Product, Variations

# Create your views here.


def index(request):
    if request.method == "GET":
        products = Product.objects.all()
        variations = Variations.objects.all()

        paginator = Paginator(products, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, "excelparser/index.html", {
            "products": products,
            "variations": variations,
            "productsCount": len(products),
            "variationsCount": len(variations),
            "paginator": page_obj
        })
    else:
        return HttpResponse('404')
    

@csrf_exempt
def addProducts(request):
    if request.method == "POST":
        excel_file = request.FILES["excel_file"]
        wb = openpyxl.load_workbook(excel_file)

        worksheet = wb["Sheet1"]
        # print(worksheet)
        for i, row in enumerate(worksheet.iter_rows()):
            if i == 0:
                continue

            product_name = row[0].value
            variation = row[1].value
            stock = row[2].value

            try:
                product = Product.objects.get(name=product_name)
            except:
                Product.objects.create(name=product_name, lowest_price=20000)

            try:
                Variations.objects.get(variation_text=variation)
            except:
                Variations.objects.create(product_ID=product, variation_text=variation, stock=stock)

        return HttpResponse('200')
    
    else:
        return HttpResponse('404')
