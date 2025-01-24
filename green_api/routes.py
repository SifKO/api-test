"""
Routers for our test Web API 
"""
from dataclasses import field
import requests
from flask import render_template, request, flash
from green_api import app, logger
from green_api.forms import ApiForm


TIMEOUT = (5, 10)
RESOURCE_URL = 'https://7105.api.greenapi.com'


def check_field(txt_field=field):
    """
    Check field and print flash messages
    """
    if not txt_field:
        flash('Проверь правильность заполнения полей')


@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    """
    Main HTML
    Performing test manipulation for Green API
    """
    form = ApiForm()

    if request.method == 'POST' and form.validate_on_submit():
        action = request.form.get('action')
        id_instance = form.id_instance.data
        api_token_instance = form.api_token_instance.data
        send_to_id = form.send_to_id.data
        send_to_id_img = form.send_to_id_img.data

        form.id_instance.data = id_instance
        form.api_token_instance.data = api_token_instance
        form.send_to_id.data = send_to_id
        form.send_to_id_img.data = send_to_id_img

        logger.info(
            "Selected act-%s, id_in-%s, token-%s, to_id-%s, img_to_id-%s",
            action, id_instance, api_token_instance, send_to_id, send_to_id_img
                    )

        actions_map = {
            'getSettings': f'/waInstance{id_instance}/getSettings/{api_token_instance}',
            'getStateInstance': f'/waInstance{id_instance}/getStateInstance/{api_token_instance}',
            'sendMessage': f'/waInstance{id_instance}/sendMessage/{api_token_instance}',
            'sendFileByUrl': f'/waInstance{id_instance}/sendFileByUrl/{api_token_instance}'
        }

        if action in actions_map:
            url = f'{RESOURCE_URL}{actions_map[action]}'

        if action == 'getSettings':
            url = f'{RESOURCE_URL}{actions_map[action]}'
            payload = {}
            headers = {}
            response = requests.request(
                "GET", url, headers=headers, data=payload, timeout=TIMEOUT
                )
            txt = response.text.encode('utf8')
            form.response.data = txt.decode('utf-8')
            return render_template('index.html', title='API', form=form)

        if action == 'getStateInstance':
            url = f'{RESOURCE_URL}{actions_map[action]}'
            payload = {}
            headers = {}
            response = requests.request("GET",
                                        url, headers=headers, data=payload,
                                        timeout=TIMEOUT)
            txt = response.text.encode('utf8')
            form.response.data = txt.decode('utf-8')
            return render_template('index.html', title='API', form=form)

        if action == 'sendMessage':
            url = f'{RESOURCE_URL}{actions_map[action]}'
            chat_id = form.send_to_id.data
            message = form.message.data
            check_field(chat_id)
            payload = {"chatId": f"{chat_id}@c.us",
                       "message": message
                       }
            headers = {
                'Content-Type': 'application/json'
                }
            response = requests.post(url, json=payload,
                                     headers=headers, timeout=TIMEOUT)
            txt = response.text.encode('utf8')
            form.response.data = txt.decode('utf-8')
            return render_template('index.html', title='API', form=form)

        if action == 'sendFileByUrl':
            url = f'{RESOURCE_URL}{actions_map[action]}'
            file_name = 'q1'
            caption = 'Discription'
            img_url = form.img_url.data
            send_to_id_img = form.send_to_id_img.data
            check_field(send_to_id_img)
            caption = "Some Caption of Pic"
            payload = {
                "chatId": f"{send_to_id_img}@c.us",
                "urlFile": img_url,
                "fileName": file_name,
                "caption": caption}
            response = requests.post(url, json=payload,
                                     timeout=TIMEOUT)
            txt = response.text.encode('utf8')
            form.response.data = txt.decode('utf-8')
            return render_template('index.html', title='API', form=form)

    return render_template('index.html', title='API', form=form)
