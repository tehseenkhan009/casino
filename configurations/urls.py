from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest')),
    path('api-token-auth', obtain_jwt_token),
    path('user/', include(('app_dir.user.urls', 'user'), namespace='user')),
    path('api/user/', include(('app_dir.user.api.urls', 'user_api'), namespace='user_api')),
    path('api/casino/', include(('app_dir.casino.api.urls', 'casino_api'), namespace='casino_api')),
    path('api/blog/', include(('app_dir.blog.api.urls', 'blog_api'), namespace='blog_api')),
    path('api/module/', include(('app_dir.module.api.urls', 'module_api'), namespace='module_api')),
    path('api/tinymce/', include('tinymce.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
