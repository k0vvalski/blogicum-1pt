from django.shortcuts import render


def about(request):

    template = 'pages/about.html'
    context = {
        'title': 'О проекте',
    }

    return render(request, template, context)


def rules(request):

    template = 'pages/rules.html'
    context = {
        'title': 'Наши правила',
    }

    return render(request, template, context)
