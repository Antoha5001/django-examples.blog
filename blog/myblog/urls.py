from django.urls import path

from .views import HomePageView, home_detail_view, share_post

app_name = 'blog'

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('<post_id>/share/', share_post, name='share_post'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/', home_detail_view, name='detail'),
	]
