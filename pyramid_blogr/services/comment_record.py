import sqlalchemy as sa
from ..models.comment_record import CommentRecord


class CommentRecordService(object):

    @classmethod
    def all(cls, request):
        query = request.dbsession.query(CommentRecord)
        return query.order_by(sa.desc(CommentRecord.created))


    @classmethod
    def by_id(cls, _id, request):
        query = request.dbsession.query(CommentRecord)
        return query.get(_id)


    @classmethod
    def by_user(cls, userid, request):
        query = request.dbsession.query(CommentRecord)
        return query.filter(CommentRecord.created_by == userid)

    
    @classmethod
    def by_post(cls, blog_id, request):
        query = request.dbsession.query(CommentRecord)
        return query.filter(CommentRecord.blog_id == blog_id).all()
