from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/health')
def health():
  return render_template('health.html')


if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5211, threaded = True, debug = True)