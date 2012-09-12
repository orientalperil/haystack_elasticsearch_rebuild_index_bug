from django.conf.urls.defaults import patterns

from my_project.my_app.views import my_view


urlpatterns = patterns('',
    (r'^$', my_view),
)
