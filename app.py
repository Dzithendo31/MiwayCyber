from flask import Flask, jsonify,request,render_template
import asyncio
#Rewnder Template is inbulinf to Flas


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hddsddqq, 🥹</p>"

@app.route("/admin")
def admin_page():
    return render_template("admin.html",users=users)

@app.get('/users')
def get_users():
    #return movies #This is without conveetting to JSON
    return jsonify(users)

@app.get('/users/<id>')
def get_user(id):
    FoundUser = next((user for user in users if user['id']==int(id)),None)
    if FoundUser == None:
        error = {'message':'User Not found'}
        return jsonify(error),404
    return jsonify(FoundUser),200


users = [
  {
      "id":12,
    "balance": "$3,946.45",
    "picture": "http://placehold.it/32x32",
    "age": 23,
    "name": "Bird Ramsey",
    "gender": "male",
    "company": "NIMON",
    "email": "birdramsey@nimon.com"
  },
  {
      "id":13,
    "balance": "$2,499.49",
    "picture": "http://placehold.it/32x32",
    "age": 31,
    "name": "Lillian Burgess",
    "gender": "female",
    "company": "LUXURIA",
    "email": "lillianburgess@luxuria.com"
  },
  {
      "id":14,
    "balance": "$2,820.18",
    "picture": "http://placehold.it/32x32",
    "age": 34,
    "name": "Kristie Cole",
    "gender": "female",
    "company": "QUADEEBO",
    "email": "kristiecole@quadeebo.com"
  },
  {
      "id":15,
    "balance": "$3,277.32",
    "picture": "http://placehold.it/32x32",
    "age": 30,
    "name": "Leonor Cross",
    "gender": "female",
    "company": "GRONK",
    "email": "leonorcross@gronk.com"
  },
  {
      "id":16,
    "balance": "$1,972.47",
    "picture": "http://placehold.it/32x32",
    "age": 28,
    "name": "Marsh Mccall",
    "gender": "male",
    "company": "ULTRIMAX",
    "email": "marshmccall@ultrimax.com"
  }
]
