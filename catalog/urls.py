from django.urls import path, include
from catalog.views import index, categories
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('catalog.urls', namespace='catalog'))
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
]