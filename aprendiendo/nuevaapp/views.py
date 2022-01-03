from django.http import response
from django.shortcuts import redirect, render, HttpResponse
from nuevaapp.models import Article

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


def crear_articulo(request, title, content, public):
    articulo= Article(
        title= title,
        content= content,
        public= public
    )
    articulo.save()
    return HttpResponse(f"Usuario Creado: {articulo.title} - {articulo.content}")

def save_article(request):
    if request.method == 'GET':
        title=request.GET['title']
        content=request.GET['content']
        public=request.GET['public']
        articulo= Article(
            title= title,
            content= content,
            public= public
        )
        articulo.save()
        return HttpResponse(f"Usuario Creado: {articulo.title} - {articulo.content}")
    else:
        return HttpResponse(f"<h2> No se puedo guardar el articulo</h2>")

def create_article(request):

    return render(request,'create_article.html')


def articulo(request):
    try:
        articulo=Article.objects.get(pk=5)
        response= f"Articulo : {articulo.title} "
    except:
        response="<h2> Articulo no encontrado </h2>"

    return HttpResponse(response)

def editar_articulo(request,id):
    try:
        articulo=Article.objects.get(pk=id)
        response= f"Articulo : {articulo.title} "
        articulo.title ="Nuevo titulo"
        articulo.content= "Nuevo contenido actulizado"
        articulo.save()
        return HttpResponse(f"Usuario Creado: {articulo.title} - {articulo.content}")

    except:
        response="<h2> Articulo no encontrado </h2>"


def articulos(request):
    articulos=Article.objects.all().order_by('-id')

    return render(request,'articulos.html',{
        'articulos' : articulos
    })

def borrar(request,id):
    articulo=Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos')