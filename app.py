import os
from flask import Flask, request, abort, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Person, Artical
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.debug = True
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/welcome')
    def welcome():
        return jsonify({
            "welcome": "you can do with this api (get person, get article, post person, post article, patch person, patch article, delete person, delete article"
        })

    @app.route('/person', methods=['GET'])
    @requires_auth('get:persons')
    def get_person(token):
        try:

            persons = Person.query.all()

            if persons is None:
                abort(404)
            return jsonify({
                'success': True,
                'person': [person.format() for person in persons]
            })

        except Exception:
            abort(422)

    @app.route('/article', methods=['GET'])
    @requires_auth('get:articles')
    def get_articals(token):

        try:

            articals = Artical.query.all()

            if articals is None:
                abort(404)

            return jsonify({
                'success': True,
                'articles': [article.format() for article in articals]
            })

        except Exception:
            abort(422)

    @app.route('/person', methods=['POST'])
    @requires_auth('post:person')
    def addNewPerson(token):

        try:

            # id = request.json.get('id', None)
            name = request.json.get('name', None)
            department = request.json.get('department', None)

            if name is None or id is None or department is None:
                abort(400)

            try:
                Person(name=name, department=department).insert()
            except Exception:
                abort(422)

            return jsonify({

                "success": True,
                "person": [person.format() for person in Person.query.all()]

            })
        except Exception:
            abort(422)

    @app.route('/article', methods=['POST'])
    @requires_auth('post:article')
    def post_articals(token):
        try:
            category = request.json.get('category', None)
            data = request.json.get('data', None)
            person_id = request.json.get('person_id', None)

            if category is None or data is None or person_id is None:
                abort(400)

            new_artical = Artical(
                data=data,
                category=category,
                person_id=person_id)
            new_artical.insert()

            return jsonify({
                "success": True,
                "article": [article.format() for article in Artical.query.all()]
            })
        except BaseException:
            abort(422)

    @app.route('/person/<person_id>', methods=['PATCH'])
    @requires_auth('patch:person')
    def pathc_person(token, person_id):

        try:

            if request.get_json() is None:
                abort(400)

            person = Person.query.filter(Person.id == person_id).one_or_none()
            # can use Person.query.get(person_id)
            if person is None:
                abort(404)

            name = request.json.get('name', None)
            department = request.json.get('department', None)

            if name and department:
                person.name = name
                person.department = department
                person.update()
            if name:
                person.name = name
                person.update()

            if department:
                person.department = department
                person.update()

            return jsonify({
                "success": True,
                "persons": [person.format() for person in Person.query.all()]
            })
        except BaseException:
            abort(422)

    @app.route('/article/<article_id>', methods=['PATCH'])
    @requires_auth('patch:article')
    def pathc_artical(token, article_id):

        try:

            if request.get_json() is None:
                abort(400)

            artical = Artical.query.filter(
                Artical.id == article_id).one_or_none()
            if artical is None:
                abort(404)

            data = request.json.get('data', None)
            category = request.json.get('category', None)
            person_id = request.json.get('Person_id', None)

            if data and category and person_id:
                artical.data = data
                artical.category = category
                artical.person_id
                artical.update()
            if data:
                artical.data = data
                artical.update()

            if category:
                artical.update()

            if person_id:
                artical.person_id = person_id
                artical.update()

            return jsonify({
                "success": True,
                "articles": [artical.format() for artical in Artical.query.all()]
            })

        except BaseException:
            abort(422)

    @app.route('/person/<person_id>', methods=['DELETE'])
    @requires_auth('delete:person')
    def delete_person(token, person_id):

        # try:

        person = Person.query.filter(Person.id == person_id).one_or_none()

        if person is None:
            abort(404)

        articals = Artical.query.filter(Artical.person_id == person_id).all()

        if articals:
            for artical in articals:
                artical.delete()

        person.delete()

        return jsonify({

            "success": True,
            "deleted_id": person_id

        })

    # except :
        # abort(422)

    @app.route('/article/<article_id>', methods=['DELETE'])
    @requires_auth('delete:article')
    def delete_artical(token, article_id):
        try:

            artical = Artical.query.filter(
                Artical.id == article_id).one_or_none()

            if artical is None:
                abort(404)

            artical.delete()

            return jsonify({

                "success": True,
                "deleted_id": article_id

            })
        except BaseException:
            abort(422)

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "Forbidden"
        }), 403

    @app.errorhandler(404)
    def resourceNotFound(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
