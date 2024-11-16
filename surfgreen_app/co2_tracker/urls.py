from django.urls import path
from surfgreen_app.co2_tracker.views import track_co2

app_name = 'co2_tracker'
urlpatterns = [
    path('1/track/', track_co2, name='track_co2'),
]