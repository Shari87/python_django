from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/dogs/(?P<pk>[0-9]+)$',
        views.get_delete_update_dog,
        name='get_delete_update_dog'
    ),
    url(
        r'^api/v1/dogs/$',
        views.get_post_dogs,
        name='get_post_dogs'
    )
]