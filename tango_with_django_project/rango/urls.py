from django.conf.urls import url
from rango import views


app_name = 'rango'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    # url(r'^category/(?P<category_name_slug>.*)/$', views.show_category, name='show_category'),
    url(r'^add_category/$', views.add_category, name='add_category'),
]