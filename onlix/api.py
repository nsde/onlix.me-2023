import blog
import tools

import flask
import random
import markupsafe

api_bp = flask.Blueprint('api_bp',
    __name__,
)

@api_bp.route('/ip')
# @cache.cached(timeout=50)
def server_ip():
    return '173.212.213.133'

@api_bp.route('/api/v1/post')
def api_text():
    return markupsafe.escape(flask.request.args.get('text'))

@api_bp.route('/api/v1/qr/<path:subpath>')
def api_qr(subpath):
    qr = tools.generate_qr
    subpath = subpath.replace(':/', '://')
    arg = flask.request.args.get

    if len(subpath) > 1024:
        flask.abort(400, 'Sorry, QR codes that long are not allowed.')

    if arg('show'): 
        return f'<img src="{qr(subpath)}">'

    try:
        return flask.send_file(qr(subpath, fg=arg('fg'), bg=arg('bg'), return_bytesio=True), mimetype='image/jpeg')
    except ValueError as e:
        flask.abort(400, str(e))

@api_bp.route('/api/v1/blog')
def api_blog():
    return flask.jsonify(blog.get_posts(with_code=False))

@api_bp.route('/api/v1/blog/<post>')
def api_blog_post(post):
    try:
        return blog.get_info(post)
    except FileNotFoundError:
        return flask.abort(404)

@api_bp.route('/api/v1/login-demo', methods=['POST'])
def login_demo():
    return {
        'form': flask.request.form,
        'data': flask.request.data,
        'json': flask.request.get_json()
    }

@api_bp.route('/api/v1/random/website')
def random_website():
    with open('static/cdn/top_250000_domains.txt', 'r') as f:
        sites = f.readlines()

    url = random.choice(sites)
    return 'https://' + url
