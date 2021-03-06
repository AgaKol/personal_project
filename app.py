from flask import Flask, app, render_template
from controllers.animals_controller import animals_blueprint
from controllers.vets_controller import vet_blueprint
from controllers.owners_controller import owners_blueprint
app = Flask(__name__)
app.register_blueprint(animals_blueprint)
app.register_blueprint(vet_blueprint)
app.register_blueprint(owners_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)