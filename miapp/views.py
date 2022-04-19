from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category
from miapp.forms import FormArticle

# Create your views here.
# MVC Modelo Vista Controlador
# MVT Modelo Template Vista

def index(request):
    return render(request, 'index.html',{
        'mi_variable': 'soy una variable desde la vista',
        'nombre': 'Javier'
    })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request):
    return render(request, 'pagina.html')
    
def contacto(request, nombre="", apellido=""):
    return render(request, 'contacto.html',{
        'nombre': nombre,
        'appellido': apellido
    })

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()

    return HttpResponse(f"Articulo Creado: <strong>{articulo.title}-{articulo.content}-{articulo.public}</strong>")

def articulo(request):

    articulo = Article.objects.get(id = 3)

    return HttpResponse(f"Articulo: <strong>{articulo.title}-{articulo.content}-{articulo.public}</strong>")

def editar_articulo(request, id):

    articulo = Article.objects.get(id = id)

    articulo.title = "titulo editado jfp"
    articulo.content = "contenido editado jfp"
    articulo.save()

    return HttpResponse(f"Articulo: <strong>{articulo.title}-{articulo.content}-{articulo.public}</strong>")


def articulos(request):

    articulos = Article.objects.all()

    return render(request, 'articulos.html', {
        'articulos': articulos
    })

def save_article(request):

    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']

        try:
            public = request.POST['public']
        except:
            public = False


        articulo = Article(
            title = title,
            content = content,
            public = public
        )

        articulo.save()
        return HttpResponse(f"Articulo Creado: <strong>{articulo.title}-{articulo.content}-{articulo.public}</strong>")
    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")


def create_article(request):

    return render(request, 'create_article.html')


# def create_full_article(request):


