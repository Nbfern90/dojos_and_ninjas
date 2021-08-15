from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/new_ninjas')
def ninjas():
    return render_template('new_ninjas.html', dojos=Dojo.get_all())


@app.route('/new_ninjas', methods=['POST'])
def new_ninjas():
    Ninja.save(request.form)
    return redirect('/dojos')
