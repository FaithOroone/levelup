from flask import Flask, json, jsonify, request, Response

app = Flask(__name__)

@app.route('/api/add', methods=['POST'])
def add_user():
    request_data=request.get_json()
    guest={
        'name':request_data['name'],
        'id':request_data['id']
    }
    guests.append(guest)
    response = Response("", 201, mimetype="application/json")
    return response


@app.route('/api/get-users')
def get_users():
    return jsonify({'dict':guests})

@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete(id):
    guest={}
    for item in guests:
        if item['id'] == id:
            guest={
                'id':item['id'],
                'name':item['name']
            }
    guests.remove(guest)

    return jsonify({'dict':guests,'deleted':guest})



guests=[
    {
        'name':'faith',
        'id':1
        }
    ,{
        'name':'eunice',
        'id':2
        }
    ]

if __name__=='__main__':
    app.run(debug=True, port=5003)