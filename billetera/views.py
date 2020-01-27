from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Balance, Movimiento, Categoria
from .forms import MovimientoForm

# Mostrar Presupuesto
def getBadget(request):
    balance = Balance.objects.all()
    return render(request, 'home.html', {"balance" : balance})

def Movement(request):
    template_name = 'crear_movimiento.html'
    form = MovimientoForm()

    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        if form.is_valid():
            form.save()
            #se afecta el balance
            balance = Balance.objects.get(pk=1)
            if request.POST['tipo'] == 2: #Gasto
                balance.saldo -= int(request.POST['monto'])
                balance.gastos += int(request.POST['monto'])
            else:
                balance.saldo += int(request.POST['monto'])
                balance.ingresos += int(request.POST['monto'])
            balance.save()
            response = HttpResponseRedirect('/')
            valor = "Este es lo que el usuario busca en la página"
            if not request.COOKIES.get('preferencia'):
                print("crea la cookie")
                response.set_cookie('preferencia', valor, max_age=30)
            else:
                print("Cookie: ", request.COOKIES['preferencia'])
            return response

    return render(request, template_name, {'form': form})
