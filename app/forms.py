from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, DateField, FloatField, IntegerField, RadioField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets import ListWidget, CheckboxInput
from flask_wtf.file import FileField, FileAllowed

class EventForm(FlaskForm):
    title = SelectField("Type:", choices=[("music", "Music"), ("comedy", "Comedy"), ("theatre", "Theatre")], validators=[DataRequired(message = "Type required")])
    location = StringField("Location: ", validators=[DataRequired(message = "Location required")])
    event_date  = DateField("Date:", validators=[DataRequired(message = "Date required")])
    ticket_price = FloatField("Ticket Price (£):", validators=[DataRequired(message = "Ticket price required"), NumberRange(min=0, message = "Ticket price must be at least £0")])
    capacity = IntegerField("Capacity:", validators=[DataRequired(message = "Capacity required"), NumberRange(min=0, message = "Capacity must be at least 0")])
    catering_ind = RadioField("Is catering required?",choices = [("yes", "Yes"), ("no", "No")],validators = [DataRequired(message = "Catering requirements required")])
    catering = SelectMultipleField(
        "If catering is required, select all that apply:",
        choices = [("soft_drinks", "Soft drinks"),
                   ("alcohol", "Alcohol"),
                   ("bar_snacks", "Bar snacks"),
                   ("meals", "Meals")],
        #The following lines allow the multiple select field to be displayed and function correctly
        option_widget = CheckboxInput(),
        widget = ListWidget(prefix_label=False)
    )
    attachment = FileField("Upload supporting file (optional)", validators = [FileAllowed(['jpg', 'png', 'pdf'], 'Images and PDFs only')])
    submit = SubmitField("Submit Event")
