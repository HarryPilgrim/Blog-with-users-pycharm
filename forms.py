from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, validators, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")



class RegisterForm(FlaskForm):
    email = EmailField("Email: ", validators=[DataRequired(), validators.Email()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    username = StringField("Username: ", validators=[DataRequired()])
    submit = SubmitField("Register")



class LoginForm(FlaskForm):
    email = EmailField("Email: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Log in")



class CommentForm(FlaskForm):
    comment = CKEditorField("Comment: ", validators=[DataRequired()])
    submit = SubmitField("Post comment")