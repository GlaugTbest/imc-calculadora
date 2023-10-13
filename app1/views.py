from django.shortcuts import render


def home(request):
    return render(request, 'imc/home.html')


def imc_gerado(request):

    pesoimc = float(request.POST.get('peso'))
    alturaimc = float(request.POST.get('altura'))

    imc = float(pesoimc / (alturaimc * alturaimc))

    if imc < 18.5:
        condicao = 'abaixo do peso'
    elif (18.5 <= imc < 25):
        condicao = 'peso normal'
    elif (25 <= imc < 30):
        condicao = 'Acima do peso'
    elif (imc > 30):
        condicao = 'Obesidade'

    return render(request, 'imc/imc_gerado.html', {"imc": imc})
