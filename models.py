from app import db
from datetime import *
from pytz import timezone
uae = timezone('Asia/Dubai')

from flask_login import UserMixin,current_user,login_user,logout_user
from flask_admin import Admin,AdminIndexView
from flask_admin.contrib.sqla import ModelView

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    dob = db.Column(db.DateTime)
    school = db.Column(db.String(100))
    country = db.Column(db.String(100))
    level_id = db.Column(db.Integer)
    created_date = db.Column(db.DateTime, default = datetime.now(uae))
    def __repr__(self):
        return self.username
class NoteMaster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer)
    video = db.Column(db.String(100))
    notes = db.Column(db.String(500))
    clef = db.Column(db.String(100))
    points = db.Column(db.Integer)
    colour_scheme = db.Column(db.String(100))
    created_date = db.Column(db.DateTime, default = datetime.now(uae))
    def __repr__(self):
        return self.level
class McqMaster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level_id = db.Column(db.Integer, db.ForeignKey('note_master.level_id'))
    question = db.Column(db.String(100))
    created_date = db.Column(db.DateTime, default = datetime.now(uae))
    def __repr__(self):
        return self.question
class McqResults(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    response = db.Column(db.String(100))
    question_id = db.Column(db.Integer, db.ForeignKey('mcq_master.question_id'))
    duration = db.Column(db.String(100))
    created_date = db.Column(db.DateTime, default = datetime.now(uae))




class AllModelView(ModelView):

    can_delete = False
    page_size = 50
    # can_create = False
    # can_edit = False
    # can_delete = False
    # column_searchable_list = ['name', 'email']
    # column_filters = ['country']
    # column_editable_list = ['name', 'last_name'] # for inline editing
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self,name,**kwargs):
        return redirect(url_for('login'),next=request.url)

class MainAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self,name,**kwargs):
        return redirect(url_for('login'),next=request.url)