from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'sign_in/$', views.sign_in, name='sign_in'),
    url(r'sign_up/$', views.sign_up, name='sign_up'),
    url(r'sign_out/$', views.sign_out, name='sign_out'),
    url(r'(?P<account_pk>\d+)/$', views.edit_profile, name='profile'),
    url(r'edit/password$', views.change_password, name='edit_password'),
    url(r'bio/$', views.bio, name='bio'),
]
