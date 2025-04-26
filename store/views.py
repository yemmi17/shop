from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()

    if category_id:
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.all()

    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})