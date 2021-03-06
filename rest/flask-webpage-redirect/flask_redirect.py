from flask import Flask, render_template, redirect, url_for,request

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"


@app.route('/hello/name/<name>')
def hello_name(name):
   return 'Hello i am %s ' % name


@app.route('/user/<name>')
def hello_user(name):
   if name !='nirosha':
      return redirect(url_for('hello'))
   else:
      return redirect(url_for('hello_name',name = name))



if __name__ == '__main__':
    app.run(debug=True)