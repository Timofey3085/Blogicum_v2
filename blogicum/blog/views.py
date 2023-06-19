from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from datetime import datetime as dt

current_time = dt.now()


def index(request) -> HttpResponse:
    template: str = 'blog/index.html'
    post_list = Post.objects.select_related(
        'author', 'location', 'category',
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=current_time).order_by()[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id) -> HttpResponse:
    template: str = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related(
            'author', 'location', 'category',
        ).filter(
            is_published=True,
            pub_date__lte=current_time,
            category__is_published=True,
            id=id))
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug) -> HttpResponse:
    template: str = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(is_published=True, slug=category_slug)
    )
    post_list = Post.objects.select_related(
        'author', 'location', 'category',
    ).filter(
        pub_date__lte=current_time,
        is_published=True,
        category=category,)
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
