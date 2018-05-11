# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import SomeForm


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SomeForm()
    if form.validate_on_submit():
        flash('Get message for message_id {}'.format(
            form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Main', form=form)
