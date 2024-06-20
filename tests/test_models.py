import pytest
from src.models import ToDoList, Todo

def test_todo_initialization():
    todo = Todo(1, 'Buy groceries')
    assert todo.id == 1
    assert todo.name == 'Buy groceries'
    assert not todo.checked

def test_todolist_initialization():
    todolist = ToDoList(1, 'Work')
    assert todolist.id == 1
    assert todolist.name == 'Work'
    assert len(todolist.todos) == 0

def test_add_todo_to_todolist():
    todolist = ToDoList(1, 'Work')
    todolist.add_todo('Write report')
    assert len(todolist.todos) == 1
    assert todolist.todos[0].name == 'Write report'





if __name__ == '__main__':
    pytest.main()
