from flask import Flask
app = Flask('app') 

@app.route('/')
def hello_world():
  return 'Hello, World!'

# default parameter values
# @app.route('/', defaults={'name':'John'})
# @app.route('/<name>')
# def hello_world(name):
#   return 'Hello, World! %s' %name

app.run(host='0.0.0.0', port=8080)
