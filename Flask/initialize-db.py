from app import db
from app.models import tables

db.drop_all()
db.create_all()