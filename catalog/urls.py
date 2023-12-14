from django.urls import path, include
from catalog.views import *
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('catalog.urls', namespace='catalog'))
    path('', index, name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_detail/<pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_update/<pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<pk>/', BlogDeleteView.as_view(), name='log_delete'),

]