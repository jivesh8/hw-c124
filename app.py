from flask import Flask,jsonify,request

app=Flask(__name__)
List=[
    {
        'id':1,
        'name':u'rahul',
        'contact':u'8800116542',
        'done':False
    },
    {
        'id':2,
        'name':u'HIRDAY',
        'contact':u'9891383123',
        'done':False
    }
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    contact={
        'id':tasks[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',""),
        'done':False
    }
    List.append(contact)
    return jsonify({
        "status":"success",
        "message":"contact added"
        },400)
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":List
    })
if (__name__=="__main__"):
    app.run(debug=True)




