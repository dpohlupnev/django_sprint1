from django.shortcuts import render


def about(request):
    template = 'pages/about.html'
    context = {'pages': about}
    return render(request, template, context)


def rules(request):
    template = 'pages/rules.html'
    context = {'pages': rules}
    return render(request, template, context)
