from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def dojos():

    return render_template("dojos.html", all_dojos=Dojo.get_all())


@app.route('/create', methods=['POST'])
def create():
    Dojo.save(request.form)
    return redirect('/dojos')


@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo_show.html', dojo=Dojo.get_ninja(data))
