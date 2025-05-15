#!/usr/bin/env python3

class MyString:
  pass

class MyString:
    def __init__(self, value=''):
        self.value = value 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ''

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        if not self._value:
            return 0
            
       
        modified_value = self._value.replace('?', '.').replace('!', '.')
        
       
        sentences = [s for s in modified_value.split('.') if s.strip()]
        
        return len(sentences)