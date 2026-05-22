from django.shortcuts import render, redirect
from core.forms import LoginForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from core.forms import LoginForm, LinkForm
from core.models import LinkModel
from django.contrib import messages

def login(request):
    if request.user.id is not None:
        return redirect("home")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.user)
            return redirect("home")
        context = {'acesso_negado': True}
        return render(request, 'login.html', {'form':form})
    return render(request, 'login.html', {'form':LoginForm()})

        
def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return render(request, 'logout.html')
    return redirect("home")


@login_required
def home(request):
    context = {}
    return render(request, 'index.html', context)


@login_required
def cadastrar_link(request):

    if request.method == 'POST':
        form = LinkForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Link cadastrado com sucesso!'
            )

            return redirect('home')

    else:
        form = LinkForm()

    context = {
        'form': form
    }

    return render(
        request,
        'cadastrar_link.html',
        context
    )

@login_required
def listar_links(request):

    links = LinkModel.objects.all()

    context = {
        'links': links
    }

    return render(
        request,
        'listar_links.html',
        context
    )

@login_required
def selecionar_link(request):

    links = LinkModel.objects.all()

    if request.method == 'POST':

        link_id = request.POST.get('link_id')

        if not link_id:

            context = {
                'links': links,
                'erro': 'Selecione um link antes de editar.'
            }

            return render(
                request,
                'selecionar_link.html',
                context
            )

        return redirect(
            'atualizar_link',
            id=link_id
        )

    context = {
        'links': links
    }

    return render(
        request,
        'selecionar_link.html',
        context
    )

@login_required
def atualizar_link(request, id):

    link = LinkModel.objects.get(id=id)

    if request.method == 'POST':

        form = LinkForm(request.POST, instance=link)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Link atualizado com sucesso!'
            )

            return redirect('home')

    else:

        form = LinkForm(instance=link)

    context = {
        'form': form
    }

    return render(
        request,
        'atualizar_link.html',
        context
    )

@login_required
def selecionar_delete(request):

    links = LinkModel.objects.all()

    if request.method == 'POST':

        link_id = request.POST.get('link_id')

        if not link_id:

            context = {
                'links': links,
                'erro': 'Selecione um link antes de excluir.'
            }

            return render(
                request,
                'selecionar_delete.html',
                context
            )

        return redirect(
            'deletar_link',
            id=link_id
        )

    context = {
        'links': links
    }

    return render(
        request,
        'selecionar_delete.html',
        context
    )

@login_required
def deletar_link(request, id):

    link = LinkModel.objects.get(id=id)

    if request.method == 'POST':

        link.delete()

        return redirect('home')

    context = {
        'link': link
    }

    return render(
        request,
        'deletar_link.html',
        context
    )