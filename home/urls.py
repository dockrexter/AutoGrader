from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$',views.login,name='login'),
    url(r'^teacher_index/$',views.teacher_index,name='teacher_index'),
    url(r'^assignment_upload/$',views.assignment_upload,name='assignment_upload'),

    url(r'^teacher_index/teacher_login$',views.teacher_login,name='teacher_login'),
    url(r'^teacher_index/teacher_signup$',views.teacher_signup,name='teacher_signup'),
    url(r'^teacher_index/teacher_login/assignment_upload$',views.assignment_upload,name='assignment_upload'),

    url(r'^login/check_login$',views.check_login,name='check_login'),
    url(r'^signup/add_signup$',views.add_signup,name='add_signup'),
    url(r'^teacher_index/teacher_login_l$',views.teacher_login_l,name='teacher_login_l'),
]