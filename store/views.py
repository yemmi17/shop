from django.shortcuts import render
from .models import Product, Category

def home(request):
    from django.shortcuts import render
from .models import Product, Category

def home(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None
    })
