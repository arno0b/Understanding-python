from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<h1>Welcome to the home page<h1>"

@app.route("/add", methods=["POST"])
def addition():
    if request.method == 'POST':
        result = request.json['num1'] + request.json['num2'] 
        return f"The summation is {result}"

if __name__ == "__main__":
    app.run('0.0.0.0', port = 5000)