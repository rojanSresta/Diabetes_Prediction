# from flask import Flask, request, jsonify
# import test
# import data

# app = Flask(__name__)
# columns = data.read_columns()

# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#     data = request.json
#     output = test.submit_form(data)
#     return jsonify(output)

# @app.route("/members")
# def members():
#     return {"members": columns}

# if __name__ == '__main__':
#     from flask_ngrok import run_with_ngrok
#     run_with_ngrok(app) 
#     app.run()


from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
import test
import data

app = Flask(__name__)
columns = data.read_columns()

@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        input_data = request.json
        print(input_data)
        output = test.submit_form(input_data)
        return jsonify({'output': output})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/members")
def members():
    return {"members": columns}

if __name__ == '__main__':
    run_with_ngrok(app)
    app.run(debug = True)
