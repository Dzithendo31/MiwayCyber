from flask import Flask, jsonify, request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from usersBP import User, db


users_list_bp = Blueprint('users_list_bp',__name__)



# Task 3: /movies-list/99 -> Display the data on the page from Azure (MSSQL)
# Movie list detail
@users_list_bp.route("/<id>")  # HOF
def movie_detail_page(id):
    filtered_user = User.query.get(id)
    #Then you can query the Policies Database base on the ID to find the client's polices

    if filtered_user:
        data = filtered_user.to_dict()
        return render_template("userdetails.html", user=data)
    else:
        return "<h1>Movie not found</h1>"

