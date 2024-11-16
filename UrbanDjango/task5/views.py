from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
users = ['Олег', 'Николай']
def registration(request):

    username = request.cleaned_data['username']
    password = request.cleaned_data['password']
    repeat_password = request.cleaned_data['repeat_password']
    age = request.cleaned_data['age']

    if password != repeat_password:
        return {'error': 'Пароли не совпадают', 'form': request}
    elif int(age) < 18:
        return {'error': 'Вы должны быть старше 18', 'form': request}
    elif username in users:
        return {'error': 'Пользователь уже существует', 'form': request}
    else:
        users.append(username)
        return {'message': f"Приветствуем, {username}!", 'form': UserRegister()}

def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            check = registration(form)
            return render(request, 'fifth_task/registration_page.html', check)
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form': form})

def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            return render(request, 'fifth_task/registration_page.html', {'error': 'Пароли не совпадают'})
        elif int(age) < 18:
            return render(request, 'fifth_task/registration_page.html', {'error': 'Вы должны быть старше 18'})
        elif username in users:
            return render(request, 'fifth_task/registration_page.html', {'error': 'Пользователь уже существует'})
        else:
            users.append(username)
            return HttpResponse(f'Приветствуем {username}')
    return render(request, 'fifth_task/registration_page.html')
