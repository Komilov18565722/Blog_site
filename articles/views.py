from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Article
from django.urls import reverse_lazy
# Create your views here.

class PostListView(ListView):
    model = Article
    template_name = 'Post_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'article_update.html'
    fields = ('title', 'summery', 'text', 'photo')
    
    def test_func(self):
        obj = self.get_object()
        return obj.auther == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        obj = self.get_object()
        return obj.auther == self.request.user or self.request.user.is_superuser


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'summery', 'text', 'photo', )

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)
    
    
    # UserPassesTestMixin, 
    # def test_func(self) :
    #     return self.request.user.is_superuser

   