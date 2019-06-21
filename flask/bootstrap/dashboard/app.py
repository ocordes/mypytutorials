"""

bootstrap demo with flask

written by: Oliver Cordes 2019-06-21
changed by: Oliver Cordes 2019-06-21

"""


from flask import Flask, render_template
from flask_bootstrap import Bootstrap  # important v4 of flask-bootstrap


bootstrap = Bootstrap()

app = Flask(__name__)

# initialize the flask modules
bootstrap.init_app(app)

@app.context_processor
def utility_processor():
    return {
             'app_name': 'Flask-Bootstrap-Demo',
             'app_version': '0.0.1',
             'app_copyright': '2019 by {}'.format('Oliver Cordes')
             }

# some demo routes

@app.route('/products', methods=['GET'])
@app.route('/users', methods=['GET'])
@app.route('/reports', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def index():
    return render_template('base.html', debug=True, title='Dashboard')


@app.route('/orders', methods=['GET'])
def base():
    return render_template('orders.html', debug=True, title='Orders')


if __name__ == '__main__':

    app.run(host='0.0.0.0',
            port=5000,
            debug=True)
