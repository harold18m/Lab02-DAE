from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'encuesta/index.html')

def ejercicio1(request):
    return render(request, 'encuesta/formulario.html')

def calcular(request):
    if request.POST['operacion'] == 'suma':
        context = {
            'valor1':request.POST['valor1'],
            'valor2':request.POST['valor2'],
            'resultado':int(request.POST['valor1'])+int(request.POST['valor2']),
            'operacion': request.POST['operacion']
        }

    elif request.POST['operacion'] =='resta':
        context = {
                    'valor1':request.POST['valor1'],
                    'valor2':request.POST['valor2'],
                    'resultado':int(request.POST['valor1'])-int(request.POST['valor2']),
                    'operacion': request.POST['operacion'],
                    }
        
    elif request.POST['operacion'] =='producto':
        context = {
                    'valor1':request.POST['valor1'],
                    'valor2':request.POST['valor2'],
                    'resultado':int(request.POST['valor1'])*int(request.POST['valor2']),
                    'operacion': request.POST['operacion'],
                    }
        
    return render(request, 'encuesta/resultado.html', context)

def ejercicio2(request):
    return render(request, 'encuesta/formulario2.html')

def calcularEdad(request):
    edad = int(request.POST['edad'])  # Convierte la edad a entero

    if edad <= 4:
        context = {
            'entrada': "Gratis"
        }
    elif edad <= 18:
        context = {
            'entrada': "5 $"
        }
    else:
        context = {
            'entrada': "10 $"
        }

    return render(request, 'encuesta/resultado2.html', context)

def ejercicio3(request):
    return render(request, 'encuesta/formulario3.html')

def calcularVolumen(request):
    altura = int(request.POST['altura']) 
    diametro = int(request.POST['diametro']) 

    context = {
        'volumen': 3.1416 * ((diametro/2)**2) *altura,
    }

    return render(request, 'encuesta/resultado3.html', context)
