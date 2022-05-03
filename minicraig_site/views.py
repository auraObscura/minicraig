from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from .models import Category, Post

# immediately redirect to categories page to both comply with requested routing structure and more closely replicate craigslist without an unneeded separate "homepage"
def straight_to_categories(request):
    return redirect("/categories")


# homepage
class Categories(ListView):
    model = Category
    template_name = "pages/index.html"
    context_object_name = "categories"


# Category CRUD classes ===========
class CategoryDetail(DetailView):
    model = Category
    template_name = "pages/category_detail.html"
    context_object_name = "category"


class NewCategory(CreateView):
    model = Category
    template_name = "pages/category_form.html"
    fields = ["c_name", "c_description"]
    success_url = reverse_lazy("home")


class UpdateCategory(UpdateView):
    model = Category
    template_name = "pages/category_edit.html"
    fields = ["c_name", "c_description"]


class DeleteCategory(DeleteView):
    model = Category
    template_name = "pages/category_delete.html"
    success_url = reverse_lazy("home")


# =============================

# Post CRUD classes ===========
class PostDetail(DetailView):
    model = Post
    template_name = "pages/post_detail.html"
    context_object_name = "post"


class NewPost(CreateView):
    model = Post
    template_name = "pages/post_form.html"
    fields = ["title", "text", "category"]


class UpdatePost(UpdateView):
    model = Post
    template_name = "pages/post_edit.html"
    fields = ["title", "text", "category"]


class DeletePost(DeleteView):
    model = Post
    template_name = "pages/post_delete.html"
    success_url = reverse_lazy("home")
