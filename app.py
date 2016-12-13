from flask import Flask, jsonify, render_template, request
from flask_httpauth import HTTPBasicAuth
import flask

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

@app.route('/employee', methods=['GET'])
def viewemployee():
    res = spcall('votecount', ())

if __name__ == "__main__":
    app.run()