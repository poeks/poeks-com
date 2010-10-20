# urls.py
import os

from django.conf.urls.defaults import *

urlpatterns = patterns("",
    (r"^$", "poeks.views.index"),
)

urlpatterns += patterns('',
(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'media').replace('\\','/'),}),
)