from django.urls import path, include

from drf_spectacular.views import SpectacularRedocView, SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('users/', include('users.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name="schema"), name="redoc", ),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui", ),
]
