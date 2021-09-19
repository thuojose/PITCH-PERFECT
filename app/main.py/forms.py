from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, RadioField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError

class PitchForm(FlaskForm):
    title = StringField('Title', validators = [Required()])
    description = TextAreaField("What would you like to pitch?", validators = [Required()])
    category = RadioField('Label', choices = [('promotionpitch', 'Promotion Pitch'), ('interviewpitch', 'Interview Pitch'), ('pickuplines', 'Pick-Up Lines'), ('productpitch', 'Product Pitch')], validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    description = TextAreaField('Add comments', validators = [Required()])
    submit = SubmitField('Submit')

class UpvoteForm(FlaskForm):
    submit = SubmitField()

class Downvote(FlaskForm):
    submit = SubmitField()