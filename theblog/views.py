# from django.urls.base import reverse
from typing import OrderedDict
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Comment, Post
from .forms import PostForm, EditPostForm, AddCommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('like_button'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html' 
    cats = Category.objects.all()
    ordering = ['post_date']
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
        
def CategoryListView(request):
    cats_list = Category.objects.all()
    return render(request, 'category_list.html', {'cats_list':cats_list})
        
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'category.html', {'cats': cats.title().replace('-', ' '), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id):
            liked = True
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    

class AddArticleView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_article.html'
    # fields = '__all__'
    # fields = ('title', 'body')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddArticleView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    


class EditArticleView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'update_blog.html'



class DeleteArticleView(DeleteView):
    model = Post
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    # fields = ('title', 'body')


class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'
    

    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy("home")
    # fields = '__all__'


    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(AddArticleView, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

