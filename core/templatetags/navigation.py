from django import template

register = template.Library()


@register.filter
def is_active(request, active_prefix):
    """
    Usage:
    {% if request|is_active:'media:photo' %}active{% endif %}
    """
    if not request or not hasattr(request, "resolver_match"):
        return False

    resolver = request.resolver_match

    if ":" in active_prefix:
        namespace, prefix = active_prefix.split(":")
        return (
            resolver.namespace == namespace
            and resolver.url_name.startswith(prefix)
        )

    return resolver.url_name.startswith(active_prefix)