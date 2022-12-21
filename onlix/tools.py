"""General helpers for the web server"""

import io
import yaml
import flask
import qrcode
import base64
import random

from typing import Union
from datetime import datetime

def generate_token(length: int=10) -> str:
    """Returns a random token with the given length."""
    return ''.join([random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(length)])

def get_ip(request): # PRIVACY NOTICE
    """Get the request IP."""
    if not request.environ.get('HTTP_X_FORWARDED_FOR'):
        return request.environ['REMOTE_ADDR']
    return request.environ['HTTP_X_FORWARDED_FOR']

def yml(path: str, edit_to=None, default={}) -> Union[dict, list, None]:
    """Reads or writes YAML."""

    path = f'{path}.yml'

    if not edit_to:
        try:
            with open(path, encoding='utf8') as f:
                return yaml.load(f.read(), Loader=yaml.SafeLoader)
        except FileNotFoundError:
            open(path, 'w', encoding='utf8').write('{}')
            return default

    with open(path, 'w', encoding='utf8') as f:
        yaml.dump(edit_to, f, sort_keys=False, default_flow_style=False, indent=4)

def unix_to_readable(unix):
    """Does what it says."""
    return datetime.utcfromtimestamp(float(unix)).strftime('%Y/%m/%d %H:%M')

def generate_qr(data, fg=None, bg=None, return_bytesio=False):
    """Renders the BytesIO string for a QR code with the given data."""
    qr_code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr_code.add_data(data)
    qr_code.make(fit=True)

    img_buf = io.BytesIO()
    qr_code.make_image(fill_color=fg or 'black', back_color=bg or 'white').save(img_buf)
    img_buf.seek(0)

    if return_bytesio:
        return img_buf

    img_data = img_buf.read()
    img_data = base64.b64encode(img_data)
    img_data = img_data.decode()

    return f'data:image/png;base64,{img_data}'

def show(template: str, **kwargs):
    """Simply renders a template."""
    return flask.render_template(template, **kwargs)
