from flask import Flask, jsonify, render_template, request
from flask_httpauth import HTTPBasicAuth
import flask

app = Flask(__name__)
auth = HTTPBasicAuth()

@app.route('/employee/<int:employeeID>/<string:employeename>/<string:gender>/<string:salary>/<string:address>', methods=['POST'])
def insertemployee(employeeID, employeename, gender, salary, address):
    res = spcall('Insert', (employeeID, employeename, gender, salary, address), True)


if __name__ == "__main__":
    app.run()