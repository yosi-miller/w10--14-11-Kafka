from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
   return 'Hello, World!'

@app.route('/api/email', methods=['POST'])
def get_emails():
   data = request.data
   print(data)
   return {'status': 'ok'}, 200


if __name__ == '__main__':
   app.run(debug=True)