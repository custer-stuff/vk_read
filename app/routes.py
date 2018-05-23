# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import SomeForm
import requests
import json
from config import Config
import re


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SomeForm()

    domain = "https://api.vk.com/method"
    access_token = Config.SECRET_KEY
    user_id = Config.USER_ID

    if form.validate_on_submit():
        flash('Get message for message_id: {}'.format(
            form.msg_id.data))

        query_params = {
            'domain': domain,
            'access_token': access_token,
            'user_id': Config.USER_ID,
            'message_ids': form.msg_id.data
        }

        query = "{domain}/messages.getById?message_ids={message_ids}&user_id={user_id}&access_token={" \
                "access_token}&v=5.53".format(**query_params)

        # Ответ от api представляет из себя структуру со много-уровневым вложением. #
        # Нас интересует первый элемент из объекта "items", тк он и будет являться текстом сообщения #
        # Код ниже занимается выгрузкой из ответа api первого элемента объекта "items" #

        msg_body = requests.get(query).json()
        data = json.dumps(msg_body)
        data_loaded = json.loads(data)
        data_response = (data_loaded["response"])
        data_item = (data_response["items"])
        data_first_item = (data_item[0])

        try:
            msg_text = (data_first_item["body"])
        except KeyError:
            msg_text = 'чет ошибка какая-то'

        # Ищем медиа-вложения в ответе. проверяя - есть ли в объекте "items" вложения типа "photo","video"
        try:
            msg_attachments = (((data_first_item["attachments"])[0])['photo'])
        except KeyError:
            try:
                msg_attachments = (((data_first_item["attachments"])[0])['video'])
            except KeyError:
                msg_attachments = 'Медиа-вложений нет'

        # img_links = re.search(r'photo_', msg_attachments)

        return render_template('main.html', title='Main', form=form, msg_body=msg_body, user_id=user_id,
                               msg_text=msg_text, msg_attachments=msg_attachments)

    if form.validate_on_submit():
        flash('Get message for message_id: {}'.format(
            form.msg_id.data))
        # flash('length is: {}'.format(
        # form.length.data))
        return redirect(url_for('index'))
    return render_template('main.html', title='Main', form=form, user_id=user_id)
