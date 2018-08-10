from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/view')
def index():
    user = {'username': 'Nirosha'}
    return render_template('base.html', title='Home',  user=user)


if __name__ == '__main__':
    app.run(debug=True)
'''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>
'''