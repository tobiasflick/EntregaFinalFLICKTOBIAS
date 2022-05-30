from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from Shopping.forms import Formulario, UserRegisterForm
from Shopping.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def locales(request):
    return render(request,"Shopping/locales.html")

def patioComidas(request):
    return render(request,"Shopping/patioComidas.html")

def cine(request):
    return render(request,"Shopping/cine.html")

def promociones(request):
    return render(request,"Shopping/promociones.html")

def inicio(request):
    avatares= Avatares.objects.filter(user=request.user.id)
    imagen = avatares[0].imagen.url
    return render(request,"Shopping/inicio.html", {'url':imagen})

def registro(request):
    return render(request,"Shopping/registro.html")


def formulario(request):
    if request.method == 'POST':
        miFormulario = Formulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            name= RegistroPromos(nombre=informacion['nombre'], edad=informacion['edad'], email=informacion['email'])
            
            name.save()
           
            return render(request, "Shopping/inicio.html")
    
    else:
        miFormulario=Formulario()
   
    return render(request, "Shopping/formulario.html", {"miFormulario":miFormulario})


#def busquedaUsuario(request):
    #return render(request, "Shopping/busquedaUsuario.html")

#def buscar(request):

    #respuesta= f"Estoy buscando el usuario: {request.GET['email'] }"

    #return HttpResponse(respuesta)



def leerSuscriptos(request):

    suscriptos= RegistroPromos.objects.all()

    contexto= {"suscriptos":suscriptos}

    return render(request, "Shopping/leerSuscriptos.html", contexto)

def borrarSuscriptos(request, suscripto_nombre):
    suscripto = RegistroPromos.objects.get(nombre=suscripto_nombre)
    suscripto.delete()

    suscriptos= RegistroPromos.objects.all()

    contexto= {"suscriptos":suscriptos}

    return render(request, "Shopping/leerSuscriptos.html", contexto)


def editarSuscriptos(request, suscripto_nombre):
    suscripto= RegistroPromos.objects.get(nombre=suscripto_nombre)

    if request.method == 'POST':
        miFormulario= Formulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data

            suscripto.nombre= informacion['nombre']
            suscripto.edad= informacion['edad']
            suscripto.email= informacion['email']

            suscripto.save()

            return render(request, "Shopping/inicio.html")
    else:
        miFormulario= RegistroPromos(initial={'nombre':suscripto.nombre, 'edad':suscripto.edad, 'email':suscripto.email})
    
    return render(request,"Shopping/editarSuscriptos.html", {"miFormulario":miFormulario, "suscripto_nombre":suscripto_nombre})


def login_request(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contraseña=form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=contraseña)

            if user:
                login(request, user)

                return render(request, "Shopping/inicio.html", {'mensaje':f"Bienvenido {user}"})

        else:
            return render(request, "Shopping/inicio.html", {'mensaje':"Error. Datos incorrectos"})
    else:
        form= AuthenticationForm()
    
    return render(request, "Shopping/login.html", {'form':form})

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username= form.cleaned_data['username']
            form.save()
            return render(request, "Shopping/inicio.html", {"mensaje":"Usuario Creado "})

    else:
        form= UserRegisterForm()
    return render(request, "Shopping/register.html", {"form":form})

def editarUsuario(request):
    usuario = request.user

    if request.method == "POST":
        miFormulario = UserRegisterForm(request.POST)

        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            
            return render(request, "Shopping/inicio.html")

    else:

        miFormulario= UserRegisterForm(initial={'username':usuario.username, 'email':usuario.email})

    return render(request, "Shopping/editarUsuario.html", {'miFormulario':miFormulario, 'usuario':usuario.username})




    