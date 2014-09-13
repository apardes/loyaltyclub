from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from api import BusinessResource, TransactionResource



v1_api = Api(api_name = 'v1')
v1_api.register(BusinessResource())
v1_api.register(TransactionResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loyaltyclub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^webapp/', include('club.urls', namespace = 'club')),
    url(r'^api/', include(v1_api.urls)),
)
