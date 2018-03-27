from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'stores', views.StoreViewSet)

urlpatterns = [
    url(r'^foo$', views.foo),
    url(r'^contact$', views.contact),
    url(r'^store$', views.store),
    url(r'^drink$', views.drink),
    url(r'^django_foo_tpl$', TemplateView.as_view(template_name='django_foo_tpl.html')),
    url(r'^index$', TemplateView.as_view(template_name='jj2app/index.html')),
    url(r'^detail$', TemplateView.as_view(template_name='jj2app/detail.html')),
    url(r'^menu_item/create$', views.MenuItemCreation.as_view(), name='menu-item-create'),
    url(r'^menu_item/detail/(?P<pk>\d+)$', views.MenuItemDetail.as_view(), name='menu-item-detail'),
    url(r'^menu_item/edit/(?P<pk>\d+)$', views.MenuItemUpdate.as_view(), name='menu-item-edit'),
    url(r'^menu_item/delete/(?P<pk>\d+)$', views.MenuItemDelete.as_view(), name='menu-item-delete'),
    url(r'^menu_item/list$', views.MenuItemList.as_view(), name='menu-item-list'),
    url(r'^rest/$', views.rest_store, name='rest_index'),
    url(r'^rest/(?P<store_id>\d+)$', views.rest_store_detail, name='rest_store_detail'),
    url(r'^api/store/$', views.StoreList.as_view(), name='api_store_list'),
    url(r'^api/store2/$', views.StoreList2.as_view(), name='api_store_list2'),
    # URL: 视图集合 /jj2app/api2/stores/
    url(r'^api2/', include(router.urls, namespace='api2')), # ViewSet
]

