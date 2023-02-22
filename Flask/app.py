from flask import Flask,request,render_template

app = Flask(__name__)

#Route
@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/aboutus')
def about_us():
    return 'API testing'

#by default, it has get but not post
@app.route("/operation", methods = ["POST"])
def operation():
    if (request.method == "POST"):
        items=request.form.getlist("item")
        total_cost = 0
        costs = []
        for i in range(1, 7):
            cost = request.form.get(f'cost{i}')
            cost = float(cost)
            costs.append(cost)
        total_cost = sum(costs)
        
        if total_cost <= 1000:
            total_cost = total_cost * 0.9
        elif total_cost > 1000 and total_cost <= 2000:
            total_cost = total_cost * 0.8
        else:
            total_cost = total_cost * 0.7

        return render_template('result.html', result = total_cost)
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)

'''The operation() function is called when a POST request is made
to the '/operation' route. This is specified in the
@app.route("/operation", methods = ["POST"]) decorator
which indicates that the route should only accept POST requests.'''

'''When a POST request is made to the '/operation' route, the operation() function
is executed, and the values of the form fields 'item' and 'cost' are retrieved
using the Flask request object. The total cost is then calculated based on the
values of the 'cost' form fields and the discount is applied.
Finally, the result is passed to a result.html template
using the Flask render_template function.'''