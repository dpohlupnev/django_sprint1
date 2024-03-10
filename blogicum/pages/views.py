from django.shortcuts import render


def about(request):
    """Функция для информации о проекте"""
    context = {'pages': about}
    return render(request, 'pages/about.html', context)


def rules(request):
    """Функция для вывода правил сообщества"""
    context = {'pages': rules}
    return render(request, 'pages/rules.html', context)
