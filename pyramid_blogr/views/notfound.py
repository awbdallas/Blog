from pyramid.view import notfound_view_config


@notfound_view_config(renderer='pyramid_blogr:templates/404.jinja2')
def notfound_view(request):
    request.response = context
    return {}

def includeme(config):
    config.scan(__name__)
