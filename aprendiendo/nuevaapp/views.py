from django.shortcuts import redirect, render, HttpResponse


# Create your views here.
layout=""""

"""
def index(request):
    html="""

    """
    year=2021
    while year <= 2050:
        if year%2==0:
            html += f"<li>{str(year)}</li>" 
        year +=1
    html+= "</ul"
    return render(request,'index.html')

def holaMundo(request):
    return render(request,'holaMundo.html')

def pagina(request,redirigir=0):
    if redirigir == 1:
        return redirect('/inicio/')
    return render(request,'pagina.html')

def contacto(request,nombre=""):
    return HttpResponse(layout+f"<h2>CONTACTO : {nombre}</h2>")
