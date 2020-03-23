from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.mail import send_mail

from .forms import EmailSharePost

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


def share(request, post_id):

	post = get_object_or_404(Blog, id=post_id, status = 'published')

	send = False

	if request.method == "POST":

		form = EmailSharePost(request.POST)

		if form.is_valid():
			
			cd = form.cleaned_data

			# print(cd['name'])

			subject = f"{cd['name']}"

			body = f"Recomended you reading: {post.title}"

			email = cd['email']

			send_mail(subject, body, 'korolev.sergei22@yandex.ru', [email])
			
			send = True

			# return render(request, 'post-share.html', {'posts': post, 'form': form})
	else:
		form = EmailSharePost()

	return render(request, 'post-share.html', {'post': post, 'form': form, 'send': send})
	# pass
	# posted = False
	# print(post_id)
	# posts = get_list_or_404(Blog, publish__year=year, publish__month=month, publish__day=day, slug=post)
	



# Create your views here.

