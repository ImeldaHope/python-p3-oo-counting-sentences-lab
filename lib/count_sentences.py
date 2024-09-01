#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ''):
    self.value = value

  @property
  def value(self):
    return self._value 
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.") 
      # return "The value must be a string."

  def ending_checker(func):
    def ending(self):
      suffix = func(self)
      return self.value.endswith(suffix)    
    return ending

  @ending_checker
  def is_sentence(self):
    return "."

  @ending_checker 
  def is_question(self):
    return "?"  

  @ending_checker  
  def is_exclamation(self):
    return "!"

  def count_sentences(self):
    delimiters = "?!"
    
    for delimiter in delimiters:
        self.value = self.value.replace(delimiter, '.')
  
    sentences = [sentence for sentence in self.value.split(".") if sentence]
    
    return len(sentences)
  
    