from django.urls import path, include
from catalog.views import index

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('catalog.urls', namespace='catalog'))
    path('', index)
]