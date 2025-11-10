from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from .models import Article
from .forms import RegisterForm, FeedbackForm, LoggedInFeedbackForm

def index(request):
    articles = Article.objects.order_by('-published_at')
    return render(request, 'news/index.html', {'articles': articles})
#index.html me bhejega articles ko


#ye wala bas details ke liye hai[DJANGO hatao bhai]
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    feedbacks = article.feedbacks.order_by('-created_at')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f"{reverse('news:login')}?next={request.path}")

        if request.user.is_authenticated:
            form = LoggedInFeedbackForm(request.POST)
            if form.is_valid():
                fb = form.save(commit=False)
                fb.article = article
                fb.name = request.user.get_full_name() or request.user.username
                fb.email = request.user.email or ''
                fb.save()
                return redirect('news:detail', pk=article.pk)
        else:
            form = FeedbackForm(request.POST)
            if form.is_valid():
                fb = form.save(commit=False)
                fb.article = article
                fb.save()
                return redirect('news:detail', pk=article.pk)
    else:
        form = LoggedInFeedbackForm() if request.user.is_authenticated else FeedbackForm()

    return render(request, 'news/detail.html', {'article': article, 'form': form, 'feedbacks': feedbacks})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'news/register.html', {'form': form})

class NewsLoginView(LoginView):
    template_name = 'news/login.html'
    redirect_authenticated_user = True

class NewsLogoutView(LogoutView):
    next_page = '/'
