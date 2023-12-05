import json
import datetime


def ad_user():
    try:
        with open('user.json', 'r') as f:
            user: list = json.load(f)
            return user
    except (FileNotFoundError, json.JSONDecodeError):
        with open('user.json', 'w') as f:
            json.dump([], f, indent=4)
            return []


class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def add_user(self):
        users = ad_user()
        if not self.user_exists():
            user = {
                'id': users[-1]['id'] + 1 if len(users) != 0 else 1,
                'name': self.name,
                'username': self.username,
                'password': self.password,
            }
            users.append(user)
            with open('user.json', 'w') as f:
                json.dump(users, f, indent=4)
            return True
        else:
            return False

    def user_exists(self):
        users: list = ad_user()
        for user in users:
            if user['name'] == self.name:
                return True
            else:
                return False


def ad_todo():
    try:
        with open('todo.json', 'r') as f:
            todo: list = json.load(f)
            return todo
    except (FileNotFoundError, json.JSONDecodeError):
        with open('todo.json', 'w') as f:
            json.dump([], f, indent=4)
            return []


class Todo:
    def __init__(self, text, expires_at, owner_id):
        self.text = text
        self.expires_at = expires_at
        self.owner_id = owner_id

    def add_todo(self):
        todos = ad_todo()
        if not self.todo_exists():
            todo = {
                'id': todos[-1]['id'] + 1 if len(todos) != 0 else 1,
                'text': self.text,
                'expires_at': self.expires_at,
                'owner_id': self.owner_id,
            }
            todos.append(todo)
            with open('todo.json', 'w') as f:
                json.dump(todos, f, indent=4)
            return True
        else:
            return False

    def todo_exists(self):
        todos: list = ad_todo()
        for todo in todos:
            if todo['text'] == self.text:
                return True
            else:
                return False
