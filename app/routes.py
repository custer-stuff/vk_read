from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    message_id = {'message_id': '123'}
    message_bodies = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Иполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', message_id=message_id, message_bodies=message_bodies)
