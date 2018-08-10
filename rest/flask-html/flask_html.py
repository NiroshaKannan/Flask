from flask import Flask, render_template, redirect, url_for,request

app = Flask(__name__, template_folder='temp')



@app.route('/mobile')
def mobile():
    return render_template('simple.html')



if __name__ == '__main__':
    app.run(debug=True)