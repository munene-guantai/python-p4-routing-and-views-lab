#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string_param>')
def print_string(string_param):
    print(string_param)
    return string_param

@app.route('/count/<int:int_param>')
def count(int_param):
    numbers = '\n'.join(map(str, range(int_param + 1)))
    return numbers

@app.route('/math/<int:num1>/+/<int:num2>')
def math_add(num1, num2):
    result = num1 + num2
    return str(result)

@app.route('/math/<int:num1>/-/<int:num2>')
def math_subtract(num1, num2):
    result = num1 - num2
    return str(result)

@app.route('/math/<int:num1>/*/<int:num2>')
def math_multiply(num1, num2):
    result = num1 * num2
    return str(result)

@app.route('/math/<int:num1>/div/<int:num2>')
def math_divide(num1, num2):
    if num2 != 0:
        result = num1 / num2
        return str(result)
    else:
        return "Error: Division by zero"

@app.route('/math/<int:num1>/%/<int:num2>')
def math_modulo(num1, num2):
    result = num1 % num2
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
