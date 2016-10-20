import datetime # default dates on models
from pyramid_blogr.models.meta import Base  #sqlalchmy
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
    DateTime,
)

from webhelpers2.date import distance_of_time_in_words # human friendly 

class CommentRecord(Base):
    __tablename__ = 'comment_entries'
    id = Column(Integer, primary_key=True)
    # Setting blog_id for where the comment is
    blog_id = Column(Integer, nullable=False)
    comment = Column(UnicodeText, default=u'')
    # Must be registered users, no Anon entries
    created_by = Column(Unicode(255), nullable=False)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)

    
    @property
    def created_in_words(self):
        return distance_of_time_in_words(self.created,
                datetime.datetime.utcnow())

