from pyramid.security import Allow, Everyone, Authenticated

"""
BlogRecordFactory is for things pertaining to actual blog posts.
No one outside of admin should be able to make modifications to any 
of the posts. 
"""
class BlogRecordFactory(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, 'admin', 'create'),
               (Allow, 'admin', 'edit'),
               (Allow, 'admin', 'delete')]


    def __init__(self, request):
        pass


"""
User Record Actions will mostly be comments. May require more fine tuning later. 
Plans are to eventually move a lot of this to groups, but I'm still get familiar with
routes and such. 
"""
class CommentFactory(object):
    __acl__ = [(Allow, Everyone, 'view'),
                (Allow, Authenticated, 'create'),
                (Allow, Authenticated, 'edit'),
                (Allow, Authenticated, 'delete')]


    def __init__(self, request):
        pass
