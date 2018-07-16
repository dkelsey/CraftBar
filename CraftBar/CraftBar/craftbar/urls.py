from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from craftbar.beer_catalogue import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'beers', views.BeerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^beers/$', views.BeerList.as_view()),
    url(r'^beers/(?P<pk>[0-9]+)$', views.BeerDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
