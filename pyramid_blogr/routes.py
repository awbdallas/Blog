def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('blog', '/blog/{id:\d+}/{slug}')
    config.add_route('blog_action', '/blog/{action}',
                     factory='pyramid_blogr.security.BlogRecordFactory')
    config.add_route('auth', '/sign/{action}')
    config.add_route('register', '/register')
    # We can add user portions later
    config.add_route('comment', '/blog/{id:\d+}/comment/{action}',
                    factory='pyramid_blogr.security.CommentFactory')
    config.scan()

