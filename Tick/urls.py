from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from tick.views import *
from tick.organizationa_members import *
from tick.tick_chat.chat import *
from tick.tick_profile.profile import *
from tick.registration import register
from tick.communicate import mail
from tick.tick_text.send_msg import *
from tick.tick_tock.tock import *
from tick.tick_text.text_reports import report_search, report_delete
from tick.tick_phonebook.phonebook import *
from tick.tick_phonebook.phonebook_send import *
from tick.tick_calendar.create_event import *
from django.contrib import admin



admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$',                main),
        url(r'^Sync_ticks/$',     sync_ticks),
        url(r'^booksearch/$',     book_search),
        url(r'^date_search/$',    date_search),
        url(r'^sync_members/$',   sync_members),
        url(r'^staff_list/$',     staff_list),
        url(r'^report_search/$',  report_search),
        url(r'^report_delete/$',  report_delete),
        url(r'^login/$',          login),
        url(r'^super_user/$',     super_user),
        url(r'^user_staff/$',     staff_user),
        url(r'^private_user/$',   private_user),
        url(r'^staff_delete',     staff_delete),
        url(r'^credit/',          credit),
        url(r'^tock/',            tock),
        url(r'^credit_deduct/',   credit_deduct),
        url(r'^user_search/',     user_search),
        url(r'^send_tick/',       send_tick),
        url(r'^reply_tick/',      reply_tick),
        url(r'^tick_delete/',     tick_delete),
        url(r'^mark_read/',       mark_read),
        url(r'^add_staff/',       add_staff),
        url(r'^phonebook/$',      phonebook),
        url(r'^sign_up/$',        register),
        url(r'^text_msging/$',    text_msg),
        url(r'^save/$',           save),
        url(r'^create_event/$',   calendar_create_event),
        url(r'^delete_event/$',   delete_event),
        url(r'^edit_event/$',     edit_an_event),
        url(r'^contact_edit/$',   contact_edit),
        url(r'^number_delete/$',  delete),
        url(r'^admin/',           include(admin.site.urls)),
        url(r'^logout/$',         logout),
        url(r'^profile_edit/$',   profile_edit),
        url(r'^change_password/$',change_password),
        url(r'^change_account/$', change_account),
        url(r'^conversation/$',   conversation),

       )
       
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

 )


