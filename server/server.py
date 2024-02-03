from flask import Flask, request, jsonify
import test
import data

app = Flask(__name__)
columns = data.read_columns()

@app.route('/result')
def result():
    return {"prediction": model_prediction}

@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        form_data = request.json
        form_data_values = list(form_data.values())
        global model_prediction
        model_prediction = test.predict(form_data_values)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/members")
def members():
    return {"members": columns}

if __name__ == '__main__':
    app.run(debug= True)
