from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Usuario
from loja.forms.UserUsuarioForm import UserUsuarioForm, UserForm
def list_usuario_view(request, id=None):
    usuarios = Usuario.objects.filter(perfil=2)
    context = {
    'usuarios': usuarios
    }
    return render(request, template_name='usuario/usuario.html', context=context, status=200)

def edit_usuario_view(request):
    print(request.user)
    usuario = get_object_or_404(Usuario, user=request.user)
    usuarioForm = UserUsuarioForm(instance=usuario)
    userForm = UserForm(instance=request.user)
    emailUnused = True
    message = None

    if request.method == 'POST':
        usuarioForm = UserUsuarioForm(request.POST, instance=usuario)
        userForm = UserForm(request.POST, instance=request.user)
        verifyEmail = Usuario.objects.filter(user__email=request.POST['email']).exclude(user__id=request.user.id).first()
        emailUnused = verifyEmail is None
    else:
        usuarioForm = UserUsuarioForm(instance=usuario)
        userForm = UserForm(instance=request.user)

    if usuarioForm.is_valid() and userForm.is_valid() and emailUnused:
        usuarioForm.save()
        userForm.save()
        message = { 'type': 'success', 'text': 'Dados atualizados com sucesso' }
    else:
        if request.method == 'POST':
            if emailUnused:
                message = { 'type': 'danger', 'text': 'Dados inválidos' }
            else:
                message = { 'type': 'warning', 'text': 'E-mail já usado' }

    context = {
    'usuarioForm': usuarioForm,
    'userForm': userForm,
    'message': message
    }
    return render(request, template_name='usuario/usuario-edit.html', context=context, status=200)