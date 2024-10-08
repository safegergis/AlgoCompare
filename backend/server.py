from flask import Flask, request, jsonify
from flask_cors import CORS
from sorts import bubble_sort,  merge_sort, quick_sort, radix_sort, linear_search

app = Flask(__name__)
CORS = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_ALLOW_ALL_ORIGINS'] = False

@app.route('/sort', methods=['POST'])
def sort_array():
    data = request.json
    array = data['array']
    target = data['target']

    sorted_array_bubble, time_taken_bubble = bubble_sort(array)
    sorted_array_merge, time_taken_merge = merge_sort(array)
    sorted_array_quick, time_taken_quick = quick_sort(array)
    sorted_array_radix, time_taken_radix = radix_sort(array)
    found, time_taken_linear = linear_search(array, target)
    response = jsonify({
        'bubble_sort': {
            'sorted_array': sorted_array_bubble,
            'time_taken': time_taken_bubble
        },
        'merge_sort': {
            'sorted_array': sorted_array_merge,
            'time_taken': time_taken_merge
        },
        'quick_sort': {
            'sorted_array': sorted_array_quick,
            'time_taken': time_taken_quick
        },
        'radix_sort': {
            'sorted_array': sorted_array_radix,
            'time_taken': time_taken_radix
        },
        'linear_search': {
            'found': found,
            'time_taken': time_taken_linear
        }
    })
    response.headers.add('Access-Control-Allow-Origin', 'https://algocompare.onrender.com')
    return response

if __name__ == '__main__':
    app.run(debug=True)


