from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from .models import User

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account created successfully. Awaiting admin approval.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(password) and user.is_active:
                    # Log in user
                    return redirect('post')  # Redirect to post view
                else:
                    messages.error(request, 'Invalid credentials or account not active.')
            except User.DoesNotExist:
                messages.error(request, 'Invalid credentials.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

from django.shortcuts import render

def home(request):
    return render(request, 'myapp/index.html')

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST['content']
        if not Post.objects.filter(user=request.user).exists():
            Post.objects.create(user=request.user, content=content)
            messages.success(request, 'Post created successfully.')
        else:
            messages.error(request, 'You can only post once.')
        return redirect('post_list')
    return render(request, 'create_post.html')

from django.core.paginator import Paginator

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 3)  # 3 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'post_list.html', {'page_obj': page_obj})