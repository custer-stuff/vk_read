# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import SomeForm
import requests
import json
from config import Config


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SomeForm()

    domain = "https://api.vk.com/method"
    access_token = Config.SECRET_KEY
    user_id = Config.USER_ID

    if form.validate_on_submit():
        query_params = {
            'domain': domain,
            'access_token': access_token,
            'user_id': Config.USER_ID,
            'message_ids': form.msg_id.data
        }

        query = "{domain}/messages.getById?message_ids={message_ids}&user_id={user_id}&access_token={" \
                "access_token}&v=5.53".format(**query_params)
        response = requests.get(query).json()
        return render_template('main.html', title='Main', form=form, response=response, user_id=user_id)

    if form.validate_on_submit():
        flash('Get message for message_id: {}'.format(
            form.msg_id.data))
        # flash('length is: {}'.format(
        # form.length.data))
        return redirect(url_for('index'))
    return render_template('main.html', title='Main', form=form, user_id=user_id)