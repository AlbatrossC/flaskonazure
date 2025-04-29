from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Azure!. My dumbass is gonna host this flask app as i am new to azure"

@app.route('/about')
def about():
    return "This is a simple Flask app hosted on Azure. hello"

if __name__ == '__main__':
    app.run(debug=True)