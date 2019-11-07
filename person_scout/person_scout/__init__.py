# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import os

import click
from flask import Flask, render_template
from flask_login import current_user
from flask_wtf.csrf import CSRFError

from person_scout.models import mongo
from person_scout.extensions import bootstrap, login_manager, moment, csrf
# from albumy.models import Role, User, Photo, Tag, Follow, Notification, Comment, Collect, Permission
from person_scout.settings import config


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('person_scout')
    
    app.config.from_object(config[config_name])
    app.config
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errorhandlers(app)
    register_shell_context(app)
    register_template_context(app)

    return app


def register_extensions(app):
    mongo.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)
    csrf.init_app(app)


def register_blueprints(app):
    from person_scout.blueprints.login import login_bp
    from person_scout.blueprints.collection_Wuxi import collection_wx
    from person_scout.blueprints.collection_Ningbo import collection_nb
    from person_scout.blueprints.collection_Hangzhou import collection_hz
    from person_scout.blueprints.collection_Suzhou import collection_sz
    from person_scout.blueprints.collection_Nanjing import collection_nj
    from person_scout.blueprints.collecction_Xuzhou import collection_xz
    from person_scout.blueprints.user_manage import user_bp
    app.register_blueprint(login_bp, url_prefix='/login')
    app.register_blueprint(collection_wx, url_prefix='/Wuxi')
    app.register_blueprint(collection_nb, url_prefix='/Ningbo')
    app.register_blueprint(collection_sz, url_prefix='/Suzhou')
    app.register_blueprint(collection_hz, url_prefix='/Hangzhou')
    app.register_blueprint(collection_nj, url_prefix='/Nanjing')
    app.register_blueprint(collection_xz, url_prefix='/Xuzhou')
    app.register_blueprint(user_bp, url_prefix='/')


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict()


def register_template_context(app):
    @app.context_processor
    def make_template_context():
        # if current_user.is_authenticated:
        #     notification_count = Notification.query.with_parent(current_user).filter_by(is_read=False).count()
        # else:
        #     notification_count = None
        return dict()


def register_errorhandlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(413)
    def request_entity_too_large(e):
        return render_template('errors/413.html'), 413

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template('errors/400.html', description=e.description), 500


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            mongo.drop_all()
            click.echo('Drop tables.')
        mongo.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    def init():
        """Initialize person_scout."""
        click.echo('Initializing the database...')
        mongo.create_all()

        click.echo('Initializing the roles and permissions...')
        Role.init_role()

        click.echo('Done.')

    @app.cli.command()
    @click.option('--user', default=10, help='Quantity of users, default is 10.')
    @click.option('--follow', default=30, help='Quantity of follows, default is 30.')
    @click.option('--photo', default=30, help='Quantity of photos, default is 30.')
    @click.option('--tag', default=20, help='Quantity of tags, default is 20.')
    @click.option('--collect', default=50, help='Quantity of collects, default is 50.')
    @click.option('--comment', default=100, help='Quantity of comments, default is 100.')
    def forge(user, follow, photo, tag, collect, comment):
        """Generate fake data."""

        from person_scout.fakes import fake_admin, fake_comment, fake_follow, fake_photo, fake_tag, fake_user, fake_collect

        mongo.drop_all()
        mongo.create_all()

        click.echo('Initializing the roles and permissions...')
        Role.init_role()
        click.echo('Generating the administrator...')
        fake_admin()
        click.echo('Generating %d users...' % user)
        fake_user(user)
        click.echo('Generating %d follows...' % follow)
        fake_follow(follow)
        click.echo('Generating %d tags...' % tag)
        fake_tag(tag)
        click.echo('Generating %d photos...' % photo)
        fake_photo(photo)
        click.echo('Generating %d collects...' % photo)
        fake_collect(collect)
        click.echo('Generating %d comments...' % comment)
        fake_comment(comment)
        click.echo('Done.')
