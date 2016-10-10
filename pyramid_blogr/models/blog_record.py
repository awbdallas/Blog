import datetime # default dates on mdels
from pyramid_blogr.models.meta import Base  #sqlalchmy
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
    DateTime,
)

from webhelpers2.text import urlify # generate slugs
from webhelpers2.date import distance_of_time_in_words # human friendly 

class BlogRecord(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique=True, nullable=False)
    body = Column(UnicodeText, default=u'')
    created_by = Column(Unicode(255), nullable=False)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)

    @property 
    def slug(self):
        return urlify(self.title)

    
    @property
    def created_in_words(self):
        return distance_of_time_in_words(self.created,
                datetime.datetime.utcnow())

