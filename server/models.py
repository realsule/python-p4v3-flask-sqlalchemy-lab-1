from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# models
#Class Definition: class Earthquake(db.Model): tells SQLAlchemy to map this class to a database table.
#SerializerMixin: If you are building an API, adding SerializerMixin (imported from sqlalchemy_serializer) allows you to easily convert your objects to JSON later.
class Earthquake(db.Model, SerializerMixin):

    __tablename__ = 'earthquakes'

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

##The __repr__ method: While you can use lambda, the standard way in Python is to define it as a method (def) inside the class so it can access self.
    def __repr__(self):
        return f"<Earthquake id={self.id} magnitude={self.magnitude} location={self.location} year={self.year}>"
    
##Indentation: All your columns (id, magnitude, etc.) must be indented inside the class so they are treated as attributes of the model.