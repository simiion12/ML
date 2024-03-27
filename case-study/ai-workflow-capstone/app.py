from model import *
import argparse
import os
import re
import sys
from flask import Flask, jsonify, request, send_from_directory
from numpy import ndarray

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

app = Flask(__name__)

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    return jsonify({'status': 1})


def convert_numpy_objects(res):
    # convert numpy objects to ensure they are serializable
    return {key: item.tolist() if isinstance(item, ndarray) else item
            for key, item in res.items()}

@app.route('/predict', methods=['POST', 'GET'])
def predict():

    # check input data
    if not request.json:
        return jsonify({'error': 'no input data provided'}), 400
    
    if 'query' not in request.json:
        return jsonify({'error': 'no query provided'}), 400
    
    # set the test flag
    test = False
    if 'mode' in request.json and request.json['mode'] == 'test':
        test = True

    # get the query
        query = request.json['query']

    result={}

    if query['country'] == 'all':
        countries = ['portugal', 'united_kingdom', 'hong_kong', 'eire',
                     'spain', 'france', 'singapore', 'norway', 'germany', 'netherlands']
    else:
        countries = query['country'].split(',')

    for country in countries:
        _result = model_predict(country, query['year'], query['month'], query['day'], test=test)
        print("Predicted revenue for {} is {}".format(
            country, _result['y_pred'][0]))
        result[country] = convert_numpy_objects(_result)

    return(jsonify(result))

@app.route('/train', methods=['GET', 'POST'])
def train():
    """
    basic predict function for the API

    the 'mode' flag provides the ability to toggle between a test version and a 
    production verion of training
    """

    # check for request data
    if not request.json:
        print("ERROR: API (train): did not receive request data")
        return jsonify(False)

    # set the test flag
    test = False
    if 'mode' in request.json and request.json['mode'] == 'test':
        test = True

    print("... training model")
    model_train(test=test)
    print("... training complete")

    return(jsonify(True))


@app.route('/logs/<filename>', methods=['GET'])
def logs(filename):
    """
    API endpoint to get logs
    """

    if not re.search(".log", filename):
        print("ERROR: API (log): file requested was not a log file: {}".format(filename))
        return jsonify([])

    log_dir = os.path.join(".", "log")
    if not os.path.isdir(log_dir):
        print("ERROR: API (log): cannot find log dir")
        return jsonify([])

    file_path = os.path.join(log_dir, filename)
    if not os.path.exists(file_path):
        print("ERROR: API (log): file requested could not be found: {}".format(filename))
        return jsonify([])

    return send_from_directory(log_dir, filename, as_attachment=True)


if __name__ == '__main__':

    # parse arguments for debug mode
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--debug", action="store_true", help="debug flask")
    args = ap.parse_args()

    if args.debug:
        app.run(debug=True, port=8080)
    else:
        app.run(host='0.0.0.0', threaded=True, port=8080)



