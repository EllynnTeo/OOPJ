from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('HomePage.html')



@app.route('/loans')
def findloans():
    return render_template('Loans.html')



if __name__ == '__main__':
    app.run()
