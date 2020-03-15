from django.shortcuts import render, get_list_or_404

from .models import Blog

from django.views.generic import TemplateView, ListView

# class HomepageView(TemplateView):
#     template_name = 'homepage.html'

class HomePageView(ListView):
    template_name = 'homepage.html'
    model = Blog
    context_object_name = 'posts'
    paginate_by = 3

    # posts = Blog.published.all()
    # return render(request, 'homepage.html', {'posts': posts})


def home_detail_view(request, year, month, day, post):
    
    posts = get_list_or_404(Blog, publish__year=year, publish__month=month, publish__day=day, slug=post)
    return render(request, 'detail.html', {'posts': posts})


def share_post(request, post_id):
    posted = False
    
    return(request, 'post-share.html', {'post_id': post_id})



# Create your views here.

