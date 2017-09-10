from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$', views.index) ,
        url(r'^register$', views.register) ,
        url(r'^login$', views.login) ,
        # url(r'^remove/(?P<id>\d+)$', views.remove) ,
        # url(r'^delete/(?P<id>\d+)$', views.delete) ,
        # url(r'^new$', views.show_new) ,
        # url(r'^add_new$', views.add_new) ,
        # url(r'^edit/(?P<id>\d+)$', views.edit, name='my_edit') ,
        # url(r'^edit_add/(?P<id>\d+)$', views.edit_add) ,
        # url(r'^description/(?P<id>\d+)$', views.description) ,
        url(r'^logoff$', views.logoff) ,
        # url(r'^show_user/(?P<id>\d+)$', views.show_user, name='my_show'),
        # url(r'^postt$', views.postt, name='my_post') ,
        # url(r'^commentt$', views.commentt, name='my_comment') ,
        # # url(r'^process_registration', views.process_registration),
        url(r'^remove/(?P<id>\d+)$', views.remove) ,

        url(r'^home$', views.home),
        url(r'^addtolist/(?P<id>\d+)$', views.addtolist) ,
        # url(r'^logout$', views.logout),
        # url(r'^new_book$', views.show_add_book_page),
        # url(r'^process_add_book$', views.process_add_book),
        # url(r'^user/(?P<user_id>\d+)$', views.show_user_profile),
        url(r'^addQuote$', views.addQuote),
        url(r'^quotedBy/(?P<id>\d+)$', views.quotedBy),
        # url(r'^delete_review/(?P<review_id>\d+)$', views.delete_review)
]
