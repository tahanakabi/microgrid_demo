from app import app
from app.forms import ParamForm, NextDayForm
from flask import render_template, flash, redirect, url_for, session
from flask import request
from A3C_plusplus import Environment, Brain, MODELS_DIRECTORY
from microgrid_env_web import MicroGridEnvWeb
import numpy as np
import pickle

enviro = None

@app.route('/index')
def index():
    return render_template('index.html', title= 'Home')


# @app.route('/parameters')
# def parameters():
#     form = ParamForm()
#     return render_template('parameters.html', title='Microgrid Parameters', form=form)
@app.route('/', methods = ['GET', 'POST'])
@app.route('/demo', methods = ['GET', 'POST'])
def parameters():
    global enviro
    enviro = None
    form = ParamForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        flash('The following data is being processed: \n')
        for fieldname, value in form.data.items():
            if fieldname!= "submit" and fieldname!="csrf_token" and value is not None:
                flash('{}={}'.format(fieldname, value))
                session[fieldname]=value
        flash('The rest of the parameters are going to take the default values')
        return redirect(url_for('graphs'))
    else:
        return render_template('parameters.html', title='Microgrid Parameters', form=form)


@app.route('/graphs',  methods=['GET', 'POST'])
def graphs():
    global enviro
    form = NextDayForm(request.form)
    if form.validate_on_submit() and request.method == "POST" and form.next_day.data:
        print("Next day")
        enviro.env.day = enviro.env.day + 1
        return redirect(url_for('graphs'))
    if form.validate_on_submit() and request.method == "POST" and form.previous_day.data:
        enviro.env.reset_all(enviro.env.day - 1)
        return redirect(url_for('graphs'))
    if enviro == None:
        print("Retrieving parameters")
        parameters = request.get_json()
        print(parameters)
        print("Initializing the environment")
        enviro = Environment(render=True, eps_start=0., eps_end=0.)
        print("Initializing the environment's environmennt")
        enviro.env = MicroGridEnvWeb(**session)
    print("Initializing the Brain")
    brain = Brain(environment=enviro)
    print("Associating the brain with the environment")
    enviro.brain = brain
    print("Running the episode")
    enviro.runEpisode(day= enviro.env.day, pplt=True, web=True)
    print("Rendering the template")
    return render_template('figure.html', title="Results", form= form)


