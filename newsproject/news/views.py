from django.shortcuts import render, redirect
from .models import NewsCategory, News
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.views import View
from django.contrib.auth.models import User


# Create your views here.
def home_page(request):
    categories = NewsCategory.objects.all()
    articles = News.objects.all()
    context = {
        'categories': categories,
        'articles': articles
    }
    return render(request, 'home.html', context)


def get_articles(request, pk):
    article = News.objects.get(id=pk)
    context = {
        'article': article
    }
    return render(request, 'articles.html', context)


def get_category(request, pk):
    exact_category = NewsCategory.objects.get(id=pk)
    article = News.objects.filter(news_category=exact_category)
    context = {
        'articles': article,
        'category': exact_category
    }
    return render(request, 'categories.html', context)


def search_article(request):
    if request.method == 'POST':
        search_name = request.POST.get('search_article')
        try:
            search_result = News.objects.get(news_headline=search_name)
            return redirect(f'articles/{search_result.id}')
        except:
            print('Не найдено')
            return redirect('/')


# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('/')
#         else:
#             form = RegisterForm()
#             return redirect('/register', {'form': form})


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': RegisterForm}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.clean_username()
            password2 = form.clean_password2()
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(username, password=password2, email=email)
            user.save()
            login(request, user)
            return redirect('/')

        context = {'form': RegisterForm}
        return render(request, self.template_name, context)


def logout_view(request):
    logout(request)
    return redirect('/')
