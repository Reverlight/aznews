from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

CATEGORY_COLORS = {
    'default': 'color1',
    'Lifestyle': 'color1',
    'Travel': 'color2',
    'Fashion': 'color3',
    'Sports': 'color4',
    'Technology': 'color4',
    'Concert': 'color1',
    'Sea Beach': 'color4',
    'Bike show': 'color3',
    'Skeping': 'color2'
}


@register.simple_tag
def get_category_color(category):
    if category not in CATEGORY_COLORS:
        return CATEGORY_COLORS['default']
    return CATEGORY_COLORS[category]
