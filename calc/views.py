from __future__ import absolute_import

from calc import calculator
from flask import Flask, request
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SERVER_NAME='localhost:5001',
)


@app.route("/", methods=['GET'])
def index():
    return "Hello World! I'm a calculator, please try me out."


@app.route("/add", methods=['GET'])
def add():
    "Takes numbers params and sums them together"
    if not request.args.getlist('numbers'):
        return "You need to give numbers to add", 400
    numbers = request.args.get('numbers')
    return str(calculator.add(numbers))


@app.route("/subtract", methods=['GET'])
def subtract():
    "Takes numbers params and subtracts them from the first"
    if not request.args.get('numbers'):
        return "You need to give numbers to subtract", 400
    numbers = request.args.getlist('numbers')
    return str(calculator.subtract(numbers))


@app.route("/multiply", methods=['GET'])
def multiply():
    "Takes numbers params and multiplies them together"
    if not request.args.get('numbers'):
        return "You need to give numbers to multiply", 400
    numbers = request.args['numbers']
    return str(calculator.multiply(numbers))


@app.route("/divide", methods=['GET'])
def divide():
    "Takes numbers params and divides them."
    if not request.args.get('numbers'):
        return "You need to give numbers to divide", 400
    return "I'm a divider"


@app.route("/exponential", methods=['GET'])
def exponential():
    "Takes numbers params and creates the exponential of them aka x^y."
    if not request.args.get('numbers'):
        return "You need to give numbers to do x^y", 400
    numbers = request.args['numbers']
    return str(calculator.exponent(numbers))


@app.route("/root", methods=['GET'])
def root():
    """Calculates the root of the inputs.
    
       Takes numbers params and finds the xth root of y where x is the first 
       number param and y is the second
    """
    if not request.args.get('numbers'):
        return "You need to give numbers to find the root.", 400
    numbers = request.args['numbers']
    return str(calculator.root(numbers))


if __name__ == "__main__":
    app.run()
