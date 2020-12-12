
from django.conf.urls import url
from .views import (CreatePackageAPIView,PackageListView,UpdatePackageAPIView,DeletePackageView)


urlpatterns= [
    url('createPackage', CreatePackageAPIView.as_view()),
    url('getPackageList',PackageListView.as_view()),
url('packageUpdate/(?P<pk>.+)', UpdatePackageAPIView.as_view(), name='package-update'),
url('packageDelete/(?P<pk>.+)', DeletePackageView.as_view(), name='package-delete')
 ]