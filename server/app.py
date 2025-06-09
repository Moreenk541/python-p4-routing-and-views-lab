#!/usr/bin/env python3

from flask import Flask,Response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return(f'{parameter}')

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers='\n'.join(str(i) for i in range(parameter)) +'\n'
    return(numbers)
    

# @app.route('/')   
# def math(num1,operation,num2):
#    result = None


#    if operation =='+':
#        result = num1 +num2
#    elif operation =='-' :
#        result = num1 - num2
#    elif operation =='*':
#        result = num1 * num2 
#    elif operation == 'div':
#         if num2 == 0:
#             return Response("Error: Division by zero.", mimetype='text/plain')
#         result = num1 / num2
#    elif operation == '%':
#         if num2 == 0:
#             return Response("Error: Modulo by zero.", mimetype='text/plain')
#         result = num1 % num2
#    else:
#         return Response("Invalid operation. Use +, -, *, div, or %.", mimetype='text/plain')

#    return Response(str(result), mimetype='text/plain')      
   
@app.route('/math/<path:parameters>')
def calculate_math(parameters):
    parts = parameters.split('/')
    if len(parts) != 3:
        return "Invalid math expression format. Expected: <number>/<operator>/<number>", 400

    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
    except ValueError:
        return "Invalid numbers provided.", 400

    result = None
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/' or operator == 'div':
        if num2 == 0:
            return "Division by zero is not allowed.", 400
        result = num1 / num2
    elif operator == '%':
        result = num1 % num2
    else:
        return "Invalid operator. Supported operators: +, -, *, /, div, %", 400

    # Convert result to integer string if it's a whole number, unless it's a division result that should be float
    if result is not None:
        if operator == '/' or operator == 'div':
            return str(float(result)) # Always return float for division
        elif result == int(result):
            return str(int(result))
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
