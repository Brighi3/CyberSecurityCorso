from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        return render_template('welcome.html', username=username)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()