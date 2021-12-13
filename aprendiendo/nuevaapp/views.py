from django.shortcuts import redirect, render, HttpResponse


# Create your views here.
layout=""""
    <h1> Sitio web con Django | Claudio Quipidlor</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">INICIO</a>
        </li>
        <li>
            <a href="/hola-mundo">HOLA</a>
        </li>
        <li>
            <a href="/pagina">PAGINA</a>
        </li>
        <li>
            <a href="/contacto">CONTACTOS</a>
        </li>
    </ul>
    <hr/>
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
