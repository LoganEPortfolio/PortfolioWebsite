from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, TelField
from wtforms.validators import DataRequired, Email, Regexp, Length
from datetime import date
import os
from pprint import pprint

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap5(app)

class ContactForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired('A name is required')])
    email = StringField('Email', validators=[DataRequired('An email is required'), Email('Email is not valid')])
    phone = TelField('Phone Number', validators=[Length(min=10, max=10)])
    message = TextAreaField('Message', validators=[DataRequired('A message is required')])
    submit = SubmitField('Submit')

@app.route('/', methods=["GET", "POST"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        form_data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'message': request.form.get('message')
        }
        pprint(form_data)
        return redirect(url_for('home'))
    return render_template('index.html', form=form)


@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=True)
