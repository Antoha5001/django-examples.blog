from django.urls import path

from .views import HomePageView, home_detail_view, share

app_name = 'blog'

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/', home_detail_view, name='detail'),
	path('share/<int:post_id>/', share, name='share_post'),
	]
