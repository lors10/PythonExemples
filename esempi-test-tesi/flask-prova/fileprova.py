from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/page1")
def sched1():
    #return "Hello from Python!"
    return render_template('data.html')

@app.route("/page2")
def sched2():
    #return "Hello from Python!"
    return render_template('data2.html')

@app.route("/page3", methods = ['GET', 'POST'])
def sched3():
    #return "Hello from Python!"
    if request.method == 'GET':
        return render_template('data.json')
    if request.method == 'POST':
        json_data = request.json
        return json_data


if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run(debug=True, port=8001)