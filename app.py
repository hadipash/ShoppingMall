import os

from flask import Flask
from DAOs import db


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='dev',
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register the database commands
    db.init_app(app)

    # apply the blueprints to the app
    import auth, account, blog, search, cart, coupon, mylist, orders, payment, product, track_delivery
    app.register_blueprint(auth.bp)
    app.register_blueprint(account.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(search.bp)
    app.register_blueprint(cart.bp)
    app.register_blueprint(mylist.bp)
    app.register_blueprint(coupon.bp)
    app.register_blueprint(orders.bp)
    app.register_blueprint(payment.bp)
    app.register_blueprint(product.bp)
    app.register_blueprint(track_delivery.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule('/', endpoint='index')

    return app
