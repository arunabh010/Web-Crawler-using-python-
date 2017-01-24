from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',

          (r'^search/$', views.search),
         )

#
# urlpatterns = patterns('',
#     # ...
#     url(r'^search-form/$', views.search_form),
#         (r'^search/$', views.search),
#     # ...