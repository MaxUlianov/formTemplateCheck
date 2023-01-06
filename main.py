from flask import Flask, request
from tinydb import TinyDB
from template_check import template_check
from type_validation import validate_types

import config

app = Flask(__name__)
app.secret_key = config.secret

db = TinyDB('db.json')


@app.route("/", methods=["GET"])
def main():
    return db.all()


@app.route("/get_form", methods=["GET", "POST"])
@app.route("/get_form/", methods=["GET", "POST"])
def get_form():
    if request.method == "GET":
        form = request.args.to_dict()

        form_val = validate_types(form)

        for template in db.all():
            name = template.pop('name')
            if template_check(template, form_val):
                return name

        return form_val

    elif request.method == "POST":
        if request.mimetype == 'application/x-www-form-urlencoded':
            form = request.form

        form_val = validate_types(form)

        for template in db.all():
            name = template.pop('name')
            if template_check(template, form_val):
                return name

        return form_val


if __name__ == "__main__":
    app.run('0.0.0.0')
