from django.shortcuts import render
def platform_view(request):
    return render(request, 'third_task/platform.html')

def cart_view(request):
    return render(request, 'third_task/cart.html')

def games_view(request):
    game1 = 'Atomiс Heart'
    game2 = 'Cyberpunk 2077'
    game3 = 'PayDay2'
    context = {
        'game1': game1,
        'game2': game2,
        'game3': game3,
    }
    return render(request, 'third_task/games.html', context=context)

