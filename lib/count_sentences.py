class MyString:
    def __init__(self, value=''):
      if not isinstance(value, str):
        print("The value must be a string.")
      self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        text = self.value.replace('!', '.').replace('?', '.')
        sentences = text.split('.')
        return len(list(filter(None, sentences)))