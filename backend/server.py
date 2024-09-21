from flask import Flask, request, jsonify
from sorts import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort

app = Flask("AlgoCompare")

@app.route('/sort', methods=['POST'])
def sort_array():
    data = request.json
    array = data.get('array', [])

