from django import template
from aznews_app.weather_api_manager import get_city_weather

register = template.Library()


@register.simple_tag
def render_city_weather(city):
    city_weather = get_city_weather(city)
    return city_weather
