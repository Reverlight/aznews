from django import template
register = template.Library()


@register.simple_tag
def get_query_set_from_to(query_set, from_, to=None):
    # If to is not provided, we get all queryset begining from
    if not to:
        query_set = query_set[from_:]
        return query_set
    query_set = query_set[from_:to]
    return query_set
