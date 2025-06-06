from flask import Flask,request,render_template

app = Flask(__name__)

# test
@app.route('/home')
def home():
    return "<h1>Hello World<h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)