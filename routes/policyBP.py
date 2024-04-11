from flask import Flask, jsonify, request, render_template, Blueprint
from models.policy import Policy
from extensions import db


policy_bp = Blueprint('policy_bp',__name__)
   
#Lets do get users
@policy_bp.get("/")
def get_policies():
    allPolicy = Policy.query.all()  # Select * from movies | movie_list iterator
    data = [policy.to_dict() for policy in allPolicy]  # list of dictionaries
    return jsonify(data)


#Get specific policy
@policy_bp.get("/<id>")
def get_policy(id):
    filter_policy = Policy.query.get(id)
    if filter_policy:
        data = filter_policy.to_dict()
        return jsonify(data)
    else:
        return jsonify({"message": "Policy not found"}), 404
    
# Handle the error scenario
@policy_bp.post("/")
def create_policy():
    data = request.json  # body
    new_policy = Policy(**data)
    try:
        db.session.add(new_policy)
        db.session.commit()
        # movies.append(new_movie)
        result = {"message": "Added successfully", "data": new_policy.to_dict()}
        return jsonify(result), 201
    except Exception as e:
        db.session.rollback()  # Undo the change
        return jsonify({"message": str(e)}), 500
    
@policy_bp.delete('/<id>')
def delete_policy(id):
    deletePolicy = Policy.query.get(id)
    if not deletePolicy:
        #Catch the client Side error
        error = {'message':'Movie Not found'}
        return jsonify(error),404
    try:
        data = deletePolicy.to_dict()
        db.session.delete(deletePolicy)

        #Then you commit
        db.session.commit()
        return jsonify({"message": "Deleted Successfully", "data": data})
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500
    
@policy_bp.put("/<id>")
def update_policy_by_id(id):
    filtered_policy = Policy.query.get(id)
    if not filtered_policy:
        return jsonify({"message": "Movie not found"}), 404
    body = request.json  # user
 
    # body - {"rating": 4}
    try:
        #Helps us avoid some weird as injections
        for key, value in body.items():
            if hasattr(filtered_policy, key):
                setattr(filtered_policy, key, value)
 
        db.session.commit()
        return jsonify(
            {"message": "Movie updated successfully!", "data": filtered_policy.to_dict()}
        )
    except Exception as e:
        db.session.rollback()  # Undo the change
        return jsonify({"message": str(e)}), 500