from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Replace with your database URI
db = SQLAlchemy(app)


# @app.route('/create_user', methods=['POST'])
# def create_user():
#     # Your code to create a new user
#     pass

# @app.route('/exercises', methods=['GET'])
# def get_exercises():
#     # Your code to retrieve exercises
#     pass



if __name__ == '__main__':
    app.run(debug=True)
