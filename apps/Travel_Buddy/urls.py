from django.conf.urls import url
from . import views           # So we can call functions from our routes!
urlpatterns = [
	## travels/ root route
	url(r'^$', views.render_home, name = 'render_home'),       # 'home' route.
	## books/add/ route
	url(r'^(?P<trip_to_join>\w+)$', views.process_trip_join, name = 'process_join'),
	url(r'^render_add/', views.render_add, name = 'render_add'),
	url(r'^process_add/', views.process_add, name = 'process_add'),
	url(r'^trip/(?P<trip_to_view>[0-9]+)$', views.render_trip_view, name = 'render_trip'),
	# url(r'^test/', views.render_book, name = 'render_book'),
	# url(r'^(?P<book_id>[0-9]+)$', views.render_book, name = 'render_book')
]
