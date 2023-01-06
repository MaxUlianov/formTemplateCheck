from flask import Flask, request
from tinydb import TinyDB, Query

import config

app = Flask(__name__)
app.secret_key = config.secret

db = TinyDB('db.json')


@app.route("/", methods=["GET"])
def main():
    return db.all()


@app.route("/get_form/", methods=["GET", "POST"])
def get_form():
    if request.method == "GET":
        print(request)
        args = request.args
        query = request.query_string
        print(f'args = {args}')
        print(f'query = {query}')

        return 'get'

    elif request.method == "POST":
        print(request)
        args = request.args
        print(f'args = {args}')
        query = request.query_string
        print(f'query = {query}')
        # for arg, value in query:
        #     print(f'arg {arg}: {value}')

        return 'post'


if __name__ == "__main__":
    app.run('0.0.0.0')
