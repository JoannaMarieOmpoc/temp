from flask import Flask, jsonify, render_template, request
from flask_httpauth import HTTPBasicAuth
import flask

app = Flask(__name__)
