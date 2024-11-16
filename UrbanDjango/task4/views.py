from django.shortcuts import render
def platform_view(request):
    return render(request, 'fourth_task/platform.html')

def cart_view(request):
    return render(request, 'fourth_task/cart.html')

def games_view(request):
    game = ["Atomic Heart", "Cyberpunk 2077", 'PayDay2']
    context = {
        'game': game,
    }
    return render(request, 'fourth_task/games.html', context=context)

def menu_view(request):
    return render(request, 'fourth_task/menu.html')