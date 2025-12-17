# server/app.py
#!/usr/bin/env python3

from flask import Flask, jsonify ,make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# views for Earthquake model
@app.route('/earthquakes/<int:id>')
def get_earthquake_by_id(id):
    # 1. Query the database for the earthquake with the specific ID
    earthquake = Earthquake.query.filter(Earthquake.id == id).first()

    # 2. Check if the earthquake exists
    if earthquake:
        # Convert the model attributes to a dictionary
        response_dict = {
            "id": earthquake.id,
            "location": earthquake.location,
            "magnitude": earthquake.magnitude,
            "year": earthquake.year
        }
        # Return the JSON response with a 200 OK status
        return make_response(jsonify(response_dict), 200)
    
    else:
        # The test expects the key "message" and a specific string format
        return make_response(
            jsonify({"message": f"Earthquake {id} not found."}), 
            404
        )
    
#magnitude
@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
def get_earthquakes_by_magnitude(magnitude): # name must match the <magnitude> above
    # Query for earthquakes >= the magnitude
    results = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    # Create the list of dictionaries
    # Note: Using the key "quakes" because that's what your test is looking for
    earthquake_list = []
    for eq in results:
        earthquake_list.append({
            "id": eq.id,
            "location": eq.location,
            "magnitude": eq.magnitude,
            "year": eq.year
        })

    # Final response structure
    response_body = {
        "count": len(results),
        "quakes": earthquake_list  # Ensure this key is 'quakes'
    }

    return make_response(jsonify(response_body), 200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
