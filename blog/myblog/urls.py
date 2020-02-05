from django.urls import path

from .views import home_page_view, home_detail_view

app_name = 'blog'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', home_detail_view, name='detail')
]
