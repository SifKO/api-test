"""
Form that I used in project 
"""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class ApiForm(FlaskForm):
    """
    Fields for my simple form
    """
    id_instance = StringField('ID instance', validators=[DataRequired()],
                              render_kw={"placeholder": "idInstance"})
    send_to_id = StringField('Send to ID',
                             render_kw={"placeholder": "Send to idInstance"})
    send_to_id_img = StringField('Send to ID img',
                                 render_kw={
                                     "placeholder": "Send to idIstance IMG"})
    img_url = StringField('img URL',
                          render_kw={"placeholder": "Input img URL"})
    api_token_instance = StringField('API instance',
                                     validators=[DataRequired()],
                                     render_kw={
                                         "placeholder": "ApiTokenInstance"})
    message = TextAreaField('Input your message',
                            render_kw={"placeholder": "Type your message!"})
    response = TextAreaField('Ответ',
                             render_kw={"placeholder": "Ответ сервера",
                                        "disabled": True})
