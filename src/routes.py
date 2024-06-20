from flask import render_template, request, redirect, url_for, flash
from models import ToDoList
import random

todolists = [ToDoList(1, "Work"), ToDoList(2, "Personal")]


def init_routes(app):
    @app.route("/", methods=["GET", "POST"])
    @app.route("/home", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            list_name = request.form["list_name"]
            if not list_name.strip():
                flash("List name cannot be empty")
                return redirect(url_for("home"))
            list_id = random.randint(1, 1000)
            new_list = ToDoList(list_id, list_name)
            todolists.append(new_list)
        return render_template("index.html", todolists=todolists)

    @app.route("/list/<int:list_id>", methods=["GET", "POST"])
    def show_list(list_id):
        selected_list = next((l for l in todolists if l.id == list_id), None)
        if request.method == "POST":
            todo_name = request.form["todo_name"]
            if not todo_name.strip():
                flash("Todo name cannot be empty")
                return redirect(url_for("show_list", list_id=list_id))
            selected_list.add_todo(todo_name)
        return render_template("list.html", todolist=selected_list, todolists=todolists)

    @app.route("/list/<int:list_id>/delete/<int:todo_id>", methods=["POST"])
    def delete_todo(list_id, todo_id):
        selected_list = next((l for l in todolists if l.id == list_id), None)
        selected_list.delete_todo(todo_id)
        return redirect(url_for("show_list", list_id=list_id))

    @app.route("/list/<int:list_id>/toggle/<int:todo_id>", methods=["POST"])
    def toggle_todo_checked(list_id, todo_id):
        selected_list = next((l for l in todolists if l.id == list_id), None)
        selected_list.check_todo(todo_id)
        return redirect(url_for("show_list", list_id=list_id))
