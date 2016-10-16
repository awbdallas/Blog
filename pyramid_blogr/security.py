from pyramid.security import Allow, Everyone, Authenticated


class BlogRecordFactory(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, 'admin', 'create'),
               (Allow, 'admin', 'edit'),
               (Allow, 'admin', 'delete')]

    def __init__(self, request):
        pass
