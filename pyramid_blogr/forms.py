from wtforms import Form, StringField, TextAreaField, validators
from wtforms import HiddenField, PasswordField
from wtforms import HiddenField

strip_filter = lambda x: x.strip() if x else None

class BlogCreateForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=255)],
            filters=[strip_filter])
    body = TextAreaField('Contents', [validators.Length(min=1)],
            filters=[strip_filter])


class BlogUpdateForm(BlogCreateForm):
    id = HiddenField()


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=255)],
        filters=[strip_filter])
    password = PasswordField('Password', [
            validators.DataRequired(),
            validators.EqualTo('confirm', message='Passwords must match)')
    ]) 
    confirm = PasswordField('Repeat Password')
    email = StringField('Email', [
        validators.DataRequired(),
        validators.Length(min=6, max=35),
        validators.Email()
    ])


class BlogCommentForm(Form):
    comment = TextAreaField('Comment', [validators.Length(min=1)],
            filters=[strip_filter])
