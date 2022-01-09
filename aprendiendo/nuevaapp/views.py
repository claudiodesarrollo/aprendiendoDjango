from django.http import response
from django.shortcuts import redirect, render, HttpResponse
from nuevaapp.models import Article
from nuevaapp.forms import FormArticle
from django.contrib import messages
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
    if request.method == 'POST':
        title=request.POST['title']
        content=request.POST['content']
        public=request.POST['public']
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

def create_full_article(request):
    formulario=FormArticle()
    if request.method=='POST':
        formulario=FormArticle(request.POST)
        if formulario.is_valid():
            data_form=formulario.cleaned_data
            title=data_form.get('title')
            content=data_form['content']
            public=data_form['public']

            articulo= Article(
                title= title,
                content= content,
                public= public
            )
            articulo.save()

            messages.success(request,f'Articulo guardado {articulo.id}')
            return redirect('articulos')
           # return HttpResponse(articulo.title+' '+articulo.content+' '+str(articulo.public))
    else:
        formulario=FormArticle()
    return render(request,'create_full_article.html',{
        'form':formulario
    })

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