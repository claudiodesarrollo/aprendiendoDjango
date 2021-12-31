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

    hasa=range(2021,2051)
    lenguajes = ['java','C++','Python','PHP','C']
    return render(request,'index.html',{
        'mi_variable':'Soy un dato en la vista',
        'lenguajes':lenguajes,
        'years':hasa
    })

def holaMundo(request):
    return render(request,'holaMundo.html')

def pagina(request,redirigir=0):
    if redirigir == 1:
        return redirect('/inicio/')
    
    nombres=['Christopher Mendoza','Alexis Lopez','Matthew Garza','Barbara Jenkins','Brent Douglas','Laura Mahoney','John Fleming','Wayne Flores','Terri Wilson','Christina Watson','Thomas Melton','Isaiah Yates','Adam Mcpherson','Melissa Figueroa','Paul Elliott','Courtney Mills','Donald Young','Natalie Little','Jared Zavala']
    return render(request,'pagina.html',{
        'nombres':nombres
    })

def contacto(request,nombre=""):
    return HttpResponse(layout+f"<h2>CONTACTO : {nombre}</h2>")
