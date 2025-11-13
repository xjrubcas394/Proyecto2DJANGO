from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Autor
from .forms import AutorModelform

# Create your views here.

def inicio(request):
    entradas = Post.objects.all()

    contexto = {'entradas':entradas}
    return render(request, 'blog/inicio.html', contexto)

def autor_nuevo(request):
    if request.method == 'POST':
        form = AutorModelform(request.POST)
        if form.is_valid():
            #Almacenar en base de datos
            # nombre = form.cleaned_data['nombre']
            # edad = form.cleaned_data['edad']
            # email = form.cleaned_data['email']

            # Autor.objects.create(nombre=nombre, edad=edad, email=email)
            form.save()
            return redirect('autores')
    else: 
        form = AutorModelform()

    estado = 'crear'
    return render(request, 'blog/autor_nuevo.html',{'form':form, 'estado':estado})

def autor_editar(request, pk):

    autor = get_object_or_404(Autor, pk=pk)

    if request.method == 'POST':
        form = AutorModelform(request.POST, instance=autor)
        if form.is_valid():

            form.save()
            return redirect('autores')
    else: 
        # autor = Autor.objects.get(pk=pk)
        autor = get_object_or_404(Autor, pk=pk)

        form = AutorModelform(instance=autor)

    estado = 'editar'
    return render(request, 'blog/autor_nuevo.html',{'form':form, 'estado':estado})

def autor_eliminar(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('autores')
    else:
        return render(request, 'blog/autor_eliminar.html', {'autor':autor})
    


def detalle_post(request,pk):
    # entrada = Post.objects.get(pk=pk)
    # contexto = {'entrada':entrada}
    # return render(request, 'blog/detalle_post.html', contexto)

    entradas = get_object_or_404(Post, pk=pk)
    contexto = {'entrada':entradas}
    return render(request, 'blog/detalle_post.html', contexto)

def autor_post(request, autor_pk):
    entradas = Post.objects.filter(autor=autor_pk)
    autor = get_object_or_404(Autor, pk=autor_pk)
    contexto = {'entrada':entradas, 'autor':autor}
    return render(request, 'blog/autor_post.html', contexto)

def autores(request):
    autores = Autor.objects.all()
    contexto = {'autores':autores}
    return render(request, 'blog/autores.html', contexto)

