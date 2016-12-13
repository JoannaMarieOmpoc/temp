from flask import Flask, jsonify, request, render_template
from flask_httpauth import HTTPBasicAuth
from model import DBconn
import sys, flask

app = Flask(__name__)
auth = HTTPBasicAuth()

@app.route('/employee/<int:employeeID>/<string:topemployeeID>/<string:employeename>/<string:gender>/<string:salary>/<string:address>', methods=['POST'])
def insertemployee(employeeID, topemployeeID, employeename, gender, salary, address):
    res = spcall('entries', (employeeID, topemployeeID, employeename, gender, salary, address), True)

@app.route('/employee/<int:employeeID>/<string:topemployeeID>/<string:employeename>/<string:gender>/<string:salary>/<string:address>', methods=['POST'])
def updateemployee(employeeID, topemployeeID, employeename, gender, salary, address):
    res = spcall('entries', (employeeID, topemployeeID, employeename, gender, salary, address), True)

@app.route('/employee', methods=['GET'])
def viewemployee():
    res = spcall('employee', ())

@app.route('/votecount', methods=['GET'])
def voteemployee():
    res = spcall('votecount', ())

@app.route('/count', methods=['GET'])
def countvote():
    resf = spcall('votecount', ())
    return jsonify({'vote': vote, 'status' : 'ok'})

@app.after_request
def add_cors(resp):
    resp.headers['Access-Control-Allow-Origin'] = flask.request.headers.get('Origin', '*')
    resp.headers['Access-Control-Allow-Credentials'] = True
    resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET, PUT, DELETE'
    resp.headers['Access-Control-Allow-Headers'] = flask.request.headers.get('Access-Control-Request-Headers',
                                                                             'Authorization')


if __name__ == "__main__":
    app.run()