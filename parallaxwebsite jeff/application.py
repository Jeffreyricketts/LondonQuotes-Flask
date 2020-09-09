from flask import Flask, render_template

application = app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run # Take out debug=True when you want to run it in production
