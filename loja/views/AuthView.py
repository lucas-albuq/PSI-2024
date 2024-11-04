from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from loja.forms.AuthForm import LoginForm
def login_view(request):
    loginForm = LoginForm()
    message = None
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                message = {'type': 'danger', 'text': 'Dados de usuário incorretos'}
    context = {
        'form': loginForm, 
        'message': message,
        'title': 'Login', 
        'button_text':'Entrar', 
        'link_text': 'Registrar', 
        'link_href': '/register'
        }
    return render(request, template_name='auth/auth.html', context=context, status=200)