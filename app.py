# created by Varshil J. Patel.
# the flask based get api for check character, which is passing in query.
# use this on local server by run this app
# this is the example for how to implement this api http://127.0.0.1:<provided port in console>/api?character=a

import secrets
from flask import Flask, request, jsonify

# create an instance of Flask()
app = Flask(__name__)

# handle error using errorhandler()
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "msg": "Not Found",
        "status": 404
    }), 404

@app.route('/api', methods=['GET'])
def returnIntASCII():
    token = request.headers.get('Authorization')
    
    # Check if token is valid
    if not is_valid_token(token):
        return jsonify({
            "msg": "Unauthorized",
            "status": 401
        }), 401

    # flag for check is api query has character
    is_api_character = False

    # get api query character
    api_character = request.args.get('character')
    if api_character:
        is_api_character = True

    # check if query exists
    if not is_api_character:
        api_ASCII_response = jsonify({
            "msg": "Wrong request",
            "ascii": -1,
            "status": 500
        })
        return api_ASCII_response

    # if query exists
    if is_api_character:
        # check length of api query
        if len(api_character) > 1:
            api_ASCII_response = jsonify({
                "msg": "Only 1 character expected",
                "ascii": -1,
                "status": 500
            })
            return api_ASCII_response
        else:
            # convert to api character into ASCII value
            api_character_ASCII = str(ord(str(api_character)))
            api_ASCII_response = jsonify({
                "msg": "Success",
                "ascii": api_character_ASCII,
                "status": 200
            })
            return api_ASCII_response

def is_valid_token(token):
    # Validate the token against authentication
    # Example: Check if the token exists in the database or matches a specific value
    valid_tokens = ["TOKEN1", "TOKEN2", "TOKEN3"]
    return token in valid_tokens

if __name__ == '__main__':
    # run app with debugging
    # app.run(debug = True)

    # run app without debugging
    app.run()
