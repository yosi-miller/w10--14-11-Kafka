from producer.producer_management import dangerous_sentences_checker

s: list[str] = {
    'sentences': ['1 Business ask forward  quality.', '2 Report care actuahostagelly situation.',
                  '3 During  recently actuahostagelly here interview reality.']
    }
r = dangerous_sentences_checker(s)


print(r)