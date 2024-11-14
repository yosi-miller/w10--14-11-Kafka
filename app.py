import atexit
from flask import Flask, request
from database.PostgreSQL.postgre_sql_connection import DB_URL, init_db
from database.PostgreSQL.postgresql_repository import get_sentences_by_email
from database.mongoDB.mongo_repository import get_all_emails
from producer.producer_management import processor_management, producer

app = Flask(__name__)

# Configure SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

with app.app_context():
    init_db()

@app.route('/all_emails')
def all_emails():
   return get_all_emails(), 200

@app.route('/api/email', methods=['POST'])
def get_emails():
   email = request.get_json()
   processor_management(email)

   return {'status': 'ok'}, 200

@app.route('/dangers_sentence/<string:email>', methods=['GET'])
def dangers_sentence(email):
   sentence = get_sentences_by_email(email)
   dangerous_sentences = [' '.join(e.sentences) for e in sentence]
   return {'sentence': dangerous_sentences}, 200


@atexit.register
def close_producer():
   producer.close()  # close the producer

if __name__ == '__main__':
   app.run(debug=True)