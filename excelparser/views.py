import os
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import openpyxl

from .models import Product, Variations

# View for mainpage
def index(request):
    if request.method == "GET":
        products = Product.objects.all()
        variations = Variations.objects.all()

        page_number = request.GET.get('page')

        return render(request, "excelparser/index.html", {
            "products": products,
            "variations": variations,
            "productsCount": len(products),
            "variationsCount": len(variations),
        })
    else:
        return HttpResponse('404')
    
# API view to add new products
@csrf_exempt
def addProducts(request):
    if request.method == "POST":
        excel_file = request.FILES["excel_file"]
        split_tup = os.path.splitext(excel_file.name)
        filext = split_tup[1]

        # Check file type
        if filext == '.xlsx' or filext == 'xls':
            pass
        else:
            return JsonResponse({"error": "Invalid file type"}, status=404)
        
        # Check file size
        file_size = round(excel_file.size / 1000000)
        if(file_size > 2):
            return JsonResponse({"error": "File size greater than 2MB"}, status=404)

        wb = openpyxl.load_workbook(excel_file)
        worksheet = wb["Sheet1"]

        # Add each product
        for i, row in enumerate(worksheet.iter_rows()):
            if i == 0:
                continue

            product_name = row[0].value
            variation = row[1].value
            stock = row[2].value
            price = row[3].value

            # Check for invalid data
            if product_name == None or variation == None or stock == None or price == None:
                return JsonResponse({"error": "Excel file contains invalid/blank data"}, status=404)

            # Create new product
            try:
                product = Product.objects.get(name=product_name)
            except:
                product = Product.objects.create(name=product_name, lowest_price=price)

            # Create new variant
            try:
                variant = Variations.objects.get(product_ID=product, variation_text=variation)
            except:
                variant = Variations.objects.create(product_ID=product, variation_text=variation, stock=stock)

            # Update lowest price
            if product.lowest_price > price:
                product.lowest_price = price
                product.save()

            # Update stock
            if stock < 0 or None:
                variant.stock = 0
                product.save()
            else:
                variant.stock = stock
                product.save()

            variant.save()

        return HttpResponse('200')
    else:
        return HttpResponse('404')
    
# API view to get product details
def getProducts(request):
    if request.method == "GET":
        products = list(Product.objects.all().values('name', 'lowest_price', 'last_updated'))

        # Format each product in usable form
        for i, product in enumerate(products):
            product["ID"] = i + 1
            product_name = product["name"]
            prod = Product.objects.get(name=product_name)
            product["last_updated"] = product["last_updated"].strftime(("%-d %b %Y %-H:%M %p %Z"))            
            
            variants = prod.variations_set.all()
            product["variantCount"] = len(variants)

            product["variations"] = []

            if len(variants) == 0:
                product["variations"].append({"variant": "", "stock": ""})
            else:
                for i in range(len(variants)):
                    product["variations"].append({"variant": variants[i].variation_text, "stock": variants[i].stock})
                
        return JsonResponse(products, safe=False)
    else:
        return HttpResponse('404')

