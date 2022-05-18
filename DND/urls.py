<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('wiki/', include('wiki.urls')),
    path('', include('board.urls'))
]
=======
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('board.urls'))

]
>>>>>>> 392ded21f4f76be087291ab133ad27a13e296933
