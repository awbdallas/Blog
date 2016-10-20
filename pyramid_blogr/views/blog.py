from pyramid.view import view_config
from pyramid.view import notfound_view_config, forbidden_view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPUnauthorized

from ..models.blog_record import BlogRecord
from ..services.blog_record import BlogRecordService
from ..models.comment_record import CommentRecord
from ..services.comment_record import CommentRecordService
from ..forms import BlogCreateForm, BlogUpdateForm, BlogCommentForm


@view_config(route_name='blog',
        renderer='pyramid_blogr:templates/view_blog.jinja2')
@view_config(route_name='comment', match_param='action=add_comment',
        renderer='pyramid_blogr:templates/view_blog.jinja2',
        permission='create')
def blog_view(request):
    blog_id = int(request.matchdict.get('id', -1))
    entry = BlogRecordService.by_id(blog_id, request)
    comments = CommentRecordService.by_post(blog_id, request)
    form = BlogCommentForm(request.POST)
    if not entry:
        return HTTPNotFound()
    if request.method == 'POST' and form.validate():
        form_entry = CommentRecord()
        form.populate_obj(entry)
        form_entry.comment = form.comment.data
        form_entry.created_by = request.authenticated_userid
        form_entry.blog_id = blog_id
        request.dbsession.add(form_entry)
        return HTTPFound(
                location=request.route_url('blog', id=entry.id, slug=entry.slug)
                )
    return {'entry': entry, 'comments': comments, 'form': form}


@view_config(route_name='blog_action', match_param='action=create',
        renderer='pyramid_blogr:templates/edit_blog.jinja2',
        permission='create')
def blog_create(request):
    entry = BlogRecord()
    form = BlogCreateForm(request.POST)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        entry.created_by = request.authenticated_userid
        request.dbsession.add(entry)
        return HTTPFound(location=request.route_url('home'))
    return {'form': form, 'action': request.matchdict.get('action')}


@view_config(route_name='blog_action', match_param='action=edit',
        renderer='pyramid_blogr:templates/edit_blog.jinja2',
        permission='create')
def blog_update(request):
    blog_id = int(request.params.get('id', -1))
    entry = BlogRecordService.by_id(blog_id, request)
    if not entry:
        return HTTPNotFound()
    form = BlogUpdateForm(request.POST, entry)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        return HTTPFound(
            location=request.route_url('blog', id=entry.id,slug=entry.slug))
    return {'form': form, 'action': request.matchdict.get('action')}
   

@view_config(route_name='blog_action', match_param='action=delete',
        permission='delete')
def blog_delete(request):
    blog_id = int(request.params.get('id', -1))
    entry = BlogRecordService.by_id(blog_id, request)
    if not entry:
        return HTTPNotFound()
    if entry.created_by == request.authenticated_userid:
        request.dbsession.delete(entry)
        return HTTPFound(location=request.route_url('home'))
    else:
        return HTTPUnauthorized()

