from flask import Flask

app = Flask(__name__)

@app.route('/thiio')
def thiio():
    return 'Hello from the random HTTP service!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)