def dangerous_sentences_checker(email):
    '''
    :param email: dict of email information with the list sentences
    :return: tuple of (mail, hostage_status, explos_status)
    '''
    # גישה לכל משפטי המייל
    sentences = email['sentences']

    # המילים המסוכנים
    dangerous_words = ["hostage", "explos"]

    # מיקום 1 כמות המילים המסוכנות מיקום 2 האינדקס של המשםט המסוכן
    very_dangerous_sentence = [0, 0]

    # סטסטוס האם נמצא המילה מסוכנת
    hostage_status = False
    explos_status = False

    for i, w in enumerate(sentences):
        words = w.split(' ')
        hostage = list(filter(lambda x: dangerous_words[0] in x, words))
        explos = list(filter(lambda x: dangerous_words[1] in x, words))

        # עדכון האם נמצא משפט עם יותר מילים מסוכנות
        if (len(hostage) + len(explos)) > very_dangerous_sentence[0]:
            very_dangerous_sentence = [len(hostage) + len(explos), i]

        # עדכון סטאסטוס חטופים ותקיפות אם נמצא המילה
        hostage_status = True if len(hostage) > 0 else hostage_status
        explos_status = True if len(explos) > 0 else explos_status

    # עדכון מיקום המשפט הכי מסוכן
    sentences[0], sentences[very_dangerous_sentence[1]] = sentences[very_dangerous_sentence[1]], sentences[0]
    email['sentences'] = sentences

    return email, hostage_status, explos_status
