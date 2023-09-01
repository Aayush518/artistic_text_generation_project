import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange

# Define the instance folder path here
INSTANCE_FOLDER_PATH = 'C:\instance'

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='your_secret_key',
    SQLALCHEMY_DATABASE_URI='sqlite:///your_database.db',
)
app.instance_path = os.path.join(os.getcwd(), INSTANCE_FOLDER_PATH)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# Define User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

# Define SavedText model
class SavedText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)

# Define CustomStyle model
class CustomStyle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    style_name = db.Column(db.String(80), nullable=False)
    font_size = db.Column(db.Integer, nullable=False)
    font_color = db.Column(db.String(7), nullable=False)

# Define RegistrationForm using Flask-WTF
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

# Define LoginForm for user login
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

# Define ProfileForm for user profile information
class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[Length(max=50)])
    email = StringField('Email', validators=[Email()])
    bio = TextAreaField('Bio', validators=[Length(max=200)])

# Define TextGenerationForm for text generation options
class TextGenerationForm(FlaskForm):
    seed_text = TextAreaField('Seed Text', validators=[DataRequired()])
    word_count = IntegerField('Word Count Limit', validators=[NumberRange(min=10, max=500)])
    temperature = FloatField('Temperature', validators=[NumberRange(min=0.1, max=2.0)])

# Routes for user registration and login
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful!', 'success')
    return redirect(url_for('login'))

# Route for user profile
@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash('Profile updated successfully!', 'success')
    return render_template('profile.html', form=form)

# Route for text generation
@app.route('/', methods=['GET', 'POST'])
def index():
    form = TextGenerationForm()
    generated_text = ""
    style_suggestions = []
    if form.validate_on_submit():
        seed_text = form.seed_text.data
        word_count_limit = form.word_count.data
        temperature = form.temperature.data
        # Add text generation logic using seed_text, word_count_limit, and temperature
        # Generate style suggestions based on the selected style
        style_suggestions = ["Suggestion 1", "Suggestion 2", "Suggestion 3"]
    return render_template('index.html', form=form, generated_text=generated_text, style_suggestions=style_suggestions)

# Route for displaying saved texts
@app.route('/saved_texts')
@login_required
def saved_texts():
    saved_texts = SavedText.query.filter_by(user_id=current_user.id).all()
    return render_template('saved_texts.html', saved_texts=saved_texts)

# Route for displaying style customization page
@app.route('/style_customization')
@login_required
def style_customization():
    return render_template('style_customization.html')

# Route for saving custom styles
@app.route('/customize_style', methods=['POST'])
@login_required
def customize_style():
    style_name = request.form['style_name']
    font_size = request.form['font_size']
    font_color = request.form['font_color']
    custom_style = CustomStyle(user_id=current_user.id, style_name=style_name, font_size=font_size, font_color=font_color)
    db.session.add(custom_style)
    db.session.commit()
    flash('Custom style saved!', 'success')
    return redirect(url_for('style_customization'))

if __name__ == '__main__':
    app.run(debug=True)
