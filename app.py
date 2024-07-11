from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! madhav prajapati skjdbcslj sd ks sdc swjd csdsmcdj sv sd ik  sj sjbjs cjs'

if __name__ == '__main__':
    app.run(debug=True)
