import random


class Todo:
    def __init__(self, id, name, checked=False):
        if not name:
            raise ValueError("Todo name cannot be empty")
        self.id = id
        self.name = name
        self.checked = checked


class ToDoList:
    def __init__(self, id, name):
        if not name:
            raise ValueError("List name cannot be empty")
        self.id = id
        self.name = name
        self.todos = []

    def add_todo(self, name):
        if not name:
            raise ValueError("Todo name cannot be empty")
        todo_id = random.randint(1, 1000)
        new_todo = Todo(todo_id, name)
        self.todos.append(new_todo)

    def delete_todo(self, todo_id):
        self.todos = [todo for todo in self.todos if todo.id != todo_id]

    def check_todo(self, todo_id):
        for todo in self.todos:
            if todo.id == todo_id:
                todo.checked = not todo.checked
                break
