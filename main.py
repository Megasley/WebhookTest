from flask import Flask, request, jsonify

app = Flask(__name__)

received_data = []

@app.route('/bot', methods=['POST'])
def handle_gravity_form_submission():
    data = request.get_json()
    received_data.append(data)
    return jsonify(received_data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
