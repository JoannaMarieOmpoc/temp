from flask import Flask, jsonify, render_template, request
from flask_httpauth import HTTPBasicAuth
import flask

app = Flask(__name__)
auth = HTTPBasicAuth()


if __name__ == "__main__":
    manager.run()