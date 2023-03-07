from flask import Flask, render_template, request
import json
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
        json_data = json.dumps(request.json)
        #json_data = str(request.json)
        with open('templates/data.json', 'w') as myFile:
            myFile.write(json_data)
        return render_template('data.json')


if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run(debug=True, port=8001)