from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PaymentForm
from .models import Pay
from django.shortcuts import redirect
# Create your views here.
@login_required(login_url='/a')
def index(request):
    if request.method == 'POST':
        user_form = PaymentForm(request.POST)
        if user_form.is_valid():
            data = user_form.cleaned_data
            p = Pay(user=request.user, course=data['course'], number_card=data['number_card'], cvv_card=data['cvv_card'], name_card=data['name_card'], phone=data['phone'], tg_nick=data['tg_nick']) 
            p.save()
            return redirect('pre_success')
    else:
        user_form = PaymentForm()
    return render(request, 'payment/index.html', {'payment_form': user_form})
@login_required(login_url='/a')
def pre_success(request):
    try:
        a = Pay.objects.all().filter(user=request.user)[0]
    except:
        return render(request, 'errors_form.html', {'error': {'name': 'Вы не оплатили курс', 'description': 'Пожалуйста, оплатите курс', "code": 402}})
    return render(request, 'payment/pre_success.html', {'fromForm': a})

@login_required(login_url='/a')
def success(request):
    try:
        a = Pay.objects.all().filter(user=request.user)[0]
    except:
        return render(request, 'errors_form.html', {'error': {'name': 'Вы не оплатили курс', 'description': 'Пожалуйста, оплатите курс', "code": 402}})
    return render(request, 'payment/success.html', {'fromForm': a})

@login_required(login_url='/a')
def unpay(request):
    try:
        a = Pay.objects.all().filter(user=request.user).delete()
        return render(request, 'payment/unpay.html', {'success': True})
    except:
        return render(request, 'payment/unpay.html', {'success': False})
    
