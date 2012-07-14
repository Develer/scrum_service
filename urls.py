from django.conf.urls.defaults import patterns, include
from MyApp.views import scrum_board, profile, dash_board, diagrams, add_entity, add, get_json
from django.contrib.auth.views import login, logout
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^$', login),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),
    (r'^accounts/profile/$', profile),
    ('^scrum_board/$', scrum_board),
    ('^dash_board/$', dash_board),
    ('^diagrams/$', diagrams),

    ('^get_json/$', get_json),

    ('^add/$', add),
    ('add_entity_form/$', add_entity),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'./media/'}),
)