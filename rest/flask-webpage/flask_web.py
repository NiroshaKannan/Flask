from flask import Flask, render_template

app = Flask(__name__, template_folder='web')

@app.route('/page')
def index():
    user = {'username': 'Nirosha'}
    posts = [
        {
            'author': {'username': 'Sharanya'},
            'body': 'Beautiful day !'
        },
        {
            'author': {'username': 'Nathira'},
            'body': 'The day is very cool!'
        }
    ]
    return render_template('web.html', title='Home',  user=user, posts=posts)


if __name__ == '__main__':
    app.run(debug=True)