'''
● כיצד ניתן לקבל את המילה הנפוצה ביותר בהודעות החשודות לפי אימייל?

תשובה - נבצע שאילתה לדאטה בייס ששמר את כל המיילים עם המילים החשודים ולסנן לפי מייל מסויים
לאחר מכן נבצע איסוף של כל המידע המילים לליסט ובעזרת פונקציה מובנת(נמצא בסטאק אובר פלו) נעשה את החיפוש ויחזור המילה השמופיעה הכי הרבה פעמים
'''
from database.PostgreSQL.postgresql_repository import get_sentences_by_email
import collections


def get_popular_word_sentences_by_email(email):
    result = get_sentences_by_email(email)
    words = []
    for e in result:
        sentences = e.sentences
        for sentence in sentences:
            words.extend(sentence.split())

    counter = collections.Counter(words)
    return counter.most_common()[0]


popular_word = get_popular_word_sentences_by_email('jeremy37@example.org')
print(popular_word)