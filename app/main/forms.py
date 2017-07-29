# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm, Form
from wtforms import StringField, TextAreaField, BooleanField,  SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from ..models import Role, User
from flaskckeditor import CKEditor



class CKEditorForm(FlaskForm, CKEditor):
    title = StringField()
    body = TextAreaField()
    submit = SubmitField(u'发布')


class NameForm(FlaskForm):
    name = StringField('What is your name??', validators=[Required()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    name = StringField(u'姓名', validators=[Length(0, 64)])
    location = StringField(u'住址', validators=[Length(0, 64)])
    about_me = TextAreaField(u'关于我')
    # avatar = FileField(u'头像')
    submit = SubmitField(u'提交')


# class UploadPhotoForm(FlaskForm):
#     photos = FileField(u'上传图片', validators=[FileAllowed(photos, u'只能上传图片！'), FileRequired(u'文件未选择！')])
#     submit = SubmitField(u'提交')


class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError(u'邮箱已注册.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError(u'用户名已存在.')


class PostForm(FlaskForm):
    body = PageDownField(u"编辑发帖", validators=[Required()])
    submit = SubmitField(u'提交')


class CommentForm(FlaskForm):
    body = StringField(u'编辑评论', validators=[Required()])
    submit = SubmitField(u'提交')