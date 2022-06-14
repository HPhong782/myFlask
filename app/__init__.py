from flask import Flask, render_template, url_for, redirect
import os

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

mydb = SQLAlchemy(app)
from app.mod_pages.controllers import mod_pages as pages_module

app.register_blueprint(pages_module)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')