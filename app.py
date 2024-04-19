
import os,json
from flask import Flask,render_template, redirect,url_for,flash,request

from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager,login_required, login_user,logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from flask_admin import Admin

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "sample.db"))

app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

from models import *
from forms import *

@login_manager.user_loader
def load_user(user_id):
# since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

admin = Admin(app,index_view=MainAdminIndexView(),template_mode='bootstrap3')
admin.add_view(AllModelView(User,db.session))
admin.add_view(AllModelView(NoteMaster,db.session))
admin.add_view(AllModelView(McqMaster,db.session))
admin.add_view(AllModelView(McqResults,db.session))


@app.route('/',methods=['GET','POST'])
@login_required
def index():
    return render_template("index.html")


@app.route('/signup',methods=['GET','POST'])
def signup():
    title = "Sign Up"
    form = SignupForm()

    #reading country json file
    with open('static/json/countries.json') as file:
        countries = json.load(file)

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first() # if this returns a user, then the email already exists in database

        if user: # if a user is found, we want to redirect back to signup page so user can try again
            flash('Username already exists')
            return redirect(url_for('signup'))

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        #new_user = User(username=form.username.data, password=generate_password_hash(form.password.data), )
        new_user = User()
        new_user.username = form.username.data
        new_user.password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        new_user.name = form.name.data
        new_user.dob = form.dob.data
        new_user.school = form.school.data
        new_user.country = request.form["country"]
        #country not included

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        # code to validate and add user to database goes here
        return redirect(url_for('login'))
    
    return render_template('signup.html',title=title,form=form,countries=countries)


@app.route('/login',methods=['GET','POST'])
def login():
        
    title = "Login"
    
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()
        print(form.username.data)
        # check if the user exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user or not check_password_hash(user.password, form.password.data):
            flash('Please check your login details and try again.')
            return redirect(url_for('login')) 
            # if the user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        login_user(user,remember=form.remember.data)
        return redirect(url_for('index'))
    
    return render_template('login.html',title = title,form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))



