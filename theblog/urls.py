from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddArticleView, EditArticleView, DeleteArticleView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddArticleView.as_view(), name="add-post"),
    path('article/edit/<int:pk>', EditArticleView.as_view(), name="edit-post"),
    path('article/<int:pk>/remove', DeleteArticleView.as_view(), name="delete-post"),
    path('add_category/', AddCategoryView.as_view(), name="add-category"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category_list', CategoryListView, name="category-list"),
    path('like/<int:pk>', LikeView, name="like-post"),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name="add-comment"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
