from flask import Flask, jsonify, reqeust

app= Flask(__name__)

numbers=[
    {
        "id":1,
        "contact": '1875649345',
        "name": 'sumedha',
        "done": False,
    },
    {
        "id": 2,
        "contact": '4567389502',
        "name": 'mannatt',
        "done": False,
    },
    {
        "id": 3,
        "contact": '4763789247',
        "name": 'fatima',
        "done": False,
    },
]
@app.route("/add-data", methods=["POST"])

def add_number():
    if not request.jason:
        return jasonify({
            "status": 'error',
            'message': 'please provide the data',
        }, 
        400
        )
    number= {
        "id": numbers[-1]['id']+1,
        'title': request.json['title'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    numbers.append(task)
    return jsonify({
        'status': 'success',
        'message': 'number added successfully!',
    })

@app.route("/get-data")

def get_number():
    return jsonify({
        "data": numbers
    })

if(__name__ == '__main__'):
    app.run(debug= True)