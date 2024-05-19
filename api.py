from flask import Flask, request, jsonify
import joblib

# Load the pre-trained model
model = joblib.load('model.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Ensure that the request is JSON and it contains the expected data
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()
    try:
    # Extract the feature from the JSON object
        gender = float(data['gender'])
        ssc_p = float(data['ssc_p'])
        ssc_b = float(data['ssc_b'])
        hsc_p = float(data['hsc_p'])
        hsc_b = float(data['hsc_b'])
        hsc_s = float(data['hsc_s'])
        degree_p = float(data['degree_p'])
        degree_t = float(data['degree_t'])
        workex = float(data['workex'])
        mba_p = float(data['mba_p'])
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Invalid input data"}), 400

    # Make predictions using the loaded model
    prediction = model.predict([[gender, ssc_p, ssc_b, hsc_p, hsc_b, hsc_s, degree_p, degree_t, workex, mba_p]])
    # Return the prediction as JSON
    species = {0: 'Not Placed', 1: 'Placed'}
    return jsonify({"prediction": species[prediction[0]]})

if __name__ == '__main__':
    app.run(host = '0.0.0.0')  # Set debug=False in a production environment