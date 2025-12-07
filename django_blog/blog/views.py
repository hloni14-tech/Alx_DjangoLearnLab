from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# Registration view
def register(request):
if request.method == 'POST':
form = UserRegisterForm(request.POST)
if form.is_valid():
user = form.save()
username = form.cleaned_data.get('username')
messages.success(request, f'Your account has been created. You can now log in, {username}!')
return redirect('login')
else:
form = UserRegisterForm()
return render(request, 'blog/register.html', {'form': form})


# Profile view & edit
@login_required
def profile(request):
if request.method == 'POST':
u_form = UserUpdateForm(request.POST, instance=request.user)
p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
if u_form.is_valid() and p_form.is_valid():
u_form.save()
p_form.save()
messages.success(request, 'Your profile has been updated successfully!')
return redirect('profile')
else:
u_form = UserUpdateForm(instance=request.user)
p_form = ProfileUpdateForm(instance=request.user.profile)


context = {
'u_form': u_form,
'p_form': p_form
}
return render(request, 'blog/profile.html', context)

ListView,DetailView,CreateView,UpdateView,DeleteView

CommentCreateView, CommentUpdateView, LoginRequiredMixin, UserPassesTestMixin, CommentDeleteView

Post.objects.filter, title__icontains, tags__name__icontains, content__icontains
# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = "post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "post_form.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author






