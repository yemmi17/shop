from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Order

def home(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()

    if category_id:
        products = Product.objects.filter(category=category_id)
        selected_category = int(category_id)
    else:
        products = Product.objects.all()
        selected_category = None

    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')

        # Сохраняем заказ
        Order.objects.create(
            product=product,
            name=name,
            phone=phone,
            comment=comment
        )

        # После отправки можно редиректить куда-нибудь
        return redirect('home')  # Или на страницу спасибо

    return render(request, 'store/product_detail.html', {
        'product': product,
    })

def contacts(request):
    return render(request, 'store/contacts.html')



def offer(request):
    return render(request, 'store/offer.html')


def privacy_policy(request):
    return render(request, 'store/privacy_policy.html')
