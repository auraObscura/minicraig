from django.urls import path

# we don't pollute our namespace with * around these parts
from .views import (
    straight_to_categories,
    CategoryDetail,
    Categories,
    PostDetail,
    NewCategory,
    NewPost,
    UpdateCategory,
    UpdatePost,
    DeleteCategory,
    DeletePost,
)

urlpatterns = [
    path("", straight_to_categories),
    path("categories/", Categories.as_view(), name="home"),
    path("categories/new", NewCategory.as_view(), name="new_cat"),
    path("categories/<int:pk>", CategoryDetail.as_view(), name="cat_detail"),
    path("categories/<int:pk>/edit", UpdateCategory.as_view(), name="edit_cat"),
    path("categories/<int:pk>/delete", DeleteCategory.as_view(), name="delete_cat"),
    path("categories/<int:pk>/posts/new", NewPost.as_view(), name="new_post"),
    path(
        "categories/<int:category>/posts/<int:pk>",
        PostDetail.as_view(),
        name="post_detail",
    ),
    path(
        "categories/<int:category>/posts/<int:pk>/edit",
        UpdatePost.as_view(),
        name="edit_post",
    ),
    path(
        "categories/<int:category>/posts/<int:pk>/delete",
        DeletePost.as_view(),
        name="delete_post",
    ),
]
