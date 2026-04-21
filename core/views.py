from django.http import HttpResponse

def robots_txt(request):
    content = """User-agent: *
Disallow: /admin/
Disallow: /static/

Sitemap: https://www.vanishreekulkarni.in/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")