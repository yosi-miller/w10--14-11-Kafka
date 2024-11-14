import atexit

from flask import Flask, request

from database.mongoDB.repository import get_all_emails
from producer.producer_management import processor_management, producer

app = Flask(__name__)

@app.route('/all_emails')
def all_emails():
   return get_all_emails(), 200

@app.route('/api/email', methods=['POST'])
def get_emails():
   email = request.get_json()
   processor_management(email)

   return {'status': 'ok'}, 200

@atexit.register
def close_producer():
   producer.close()  # close the producer

if __name__ == '__main__':
   app.run(debug=True)