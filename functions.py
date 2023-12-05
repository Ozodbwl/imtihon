from main import User, Todo, ad_user, ad_todo
import datetime


def register():
    first_name = input('Enter your fist_name: ')
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    user = User(first_name, username, password)
    return user.add_user()


def register_t():
    text = input('Enter text: ')
    expires_at = str(datetime.datetime.now())
    owner_id = input('Enter your id: ')
    todo = Todo(text, expires_at, owner_id)
    return todo.add_todo()


def login():
    username = input('Enter username: ')
    password = input('Enter password: ')

    users = ad_user()
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user['id']
        else:
            print("password or username incorrect")
            break



