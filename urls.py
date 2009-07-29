from django.conf.urls.defaults import *

from financa.views import financ, extrato, contabanco


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^desp/', include('desp.foo.urls')),

    # Uncomment the next line to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line for to enable the admin:
     (r'^admin/(.*)', admin.site.root),
    
    #meu primeiro programa sozinho.
    (r'^financ/$', financ),
    
    (r'^financ/lanctos/$', extrato),
    
    (r'^financ/contas/$', contabanco),
    
)
