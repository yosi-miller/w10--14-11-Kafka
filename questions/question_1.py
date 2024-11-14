'''
כיצד ניתן להפיק את התוכן המלא של אובייקט לפי אימייל מסוים כולל תוכן חשוד?

תשובה - נבצע שאילתה לדאטה בייס ששמר את כל המיילים עם המילים החשודים ולסנן לפי מייל מסויים
'''
from database.PostgreSQL.postgresql_repository import get_sentences_by_email


def get_dangerous_sentences_by_email(email):
    result = get_sentences_by_email(email)
    dangerous_sentences = [{'email': e.email, 'sentences': e.sentences} for e in result ]
    return dangerous_sentences

r = get_dangerous_sentences_by_email('jeremy37@example.org')

print(r)