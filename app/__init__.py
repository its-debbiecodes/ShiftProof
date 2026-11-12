
from flask import Flask,render_template
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/features')
    def features():
        return render_template(
            'features.html',
            app_naame="ShiftProof",
            features=[
                "Track working hours",
                "Calculate expected wages",
                "compare wages with payslip",
                "Generate wage reports"
            ]
        )

    return app