import tools

import flask
import secure
import random

def manage(app: flask.Flask, *args, **kwargs):
    app.secret_key = random.sample('sdf8sdfOH_ipc-smMs.SAMIOsdumaoxnU..os-dfu.xnu', 26)
    secure_headers = secure.Secure()

    @app.after_request
    def set_secure_headers(response):
        secure_headers.framework.flask(response)
        return response

    @app.errorhandler(404)
    def error_404(error):
        rq = flask.request
        current_path = rq.path[1:]

        redirects = tools.yml('config/redirects')
        
        if current_path in redirects.keys():
            list(flask.request.args.keys())[0] if flask.request.args.keys() else False
            return flask.redirect(redirects[current_path])
        
        template = f'{current_path.replace(".closed", "")}.html'

        try:
            return tools.show(template, notice='Auto-rendered this page.')
        except Exception as e:
            if template == str(e):
                return tools.show('error.html', title='Path or file not found!', description=f'Sorry, you probably visited an old or invalid site!')
            return tools.show('error.html', title='Problems with the template', description=f'Sorry, this isn\'t your fault! An issue occurred while trying to render the template.')

    @app.after_request
    def add_cors_headers(response):
        if flask.request.path.startswith('/cdn/'):
            add_header = response.headers.add

            add_header('Access-Control-Allow-Origin', '*')
            add_header('Access-Control-Allow-Credentials', 'true')
            add_header('Access-Control-Allow-Headers', 'Content-Type')
            add_header('Access-Control-Allow-Headers', 'Cache-Control')
            add_header('Access-Control-Allow-Headers', 'X-Requested-With')
            add_header('Access-Control-Allow-Headers', 'Authorization')
            add_header('Access-Control-Allow-Methods', 'GET')
        
        return response
