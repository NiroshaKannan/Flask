from flask import Flask, render_template, redirect, url_for,request

app = Flask(__name__, template_folder='temp')


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route('/mobile')
def mobile():
    return render_template('simple.html')


@app.route('/hello/name/<name>')
def hello_name(name):
   return 'Hello i am %s ' % name

@app.route('/user/<name>')
def hello_user(name):
   if name !='nirosha':
      return redirect(url_for('hello'))
   else:
      return redirect(url_for('hello_name',name = name))


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
  

if __name__ == '__main__':
    app.run(debug=True)