from django.shortcuts import render, get_list_or_404

from .models import Blog

from django.views.generic import TemplateView

# class HomepageView(TemplateView):
#     template_name = 'homepage.html'

def home_page_view(request):
    posts = Blog.published.all()
    return render(request, 'homepage.html', {'posts': posts})


def home_detail_view(request, year, month, day, post):
    posts = get_list_or_404(Blog, publish__year=year, publish__month=month, publish__day=day, slug=post)
    return render(request, 'detail.html', {'posts': posts})




# Create your views here.

