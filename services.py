import collections
from database.PostgreSQL.postgresql_repository import get_all_sentences, get_sentences_by_email


def get_popular_word_sentences():
    result = get_all_sentences()

    words = []
    for e in result:
        sentences = e.sentences
        for sentence in sentences:
            words.extend(word.lower() for word in sentence.split())

    counter = collections.Counter(words)
    return counter.most_common()[0]

def dangerous_sentences_by_email(email):
    sentence = get_sentences_by_email(email)
    dangerous_sentences = [' '.join(e.sentences) for e in sentence]

    return dangerous_sentences

if __name__ == '__main__':
    popular_word = get_popular_word_sentences()
    print(popular_word)
