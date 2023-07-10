from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username and password:
        print(f"Username: {username}, Password: {password}")
        return "Dati di accesso ricevuti correttamente."
    return '''
        <form method="get">
            <p>Username: <input type="text" name="username"></p>
            <p>Password: <input type="password" name="password"></p>
            <p><input type="submit" value="Accedi"></p>
        </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)
