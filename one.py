class One:
 naga = 'raj'
 mano = []

 def __init__(self):
  pass
 
 def add_access(self, add):
  self.mano.append(add)
  self.naga = 'kar'

class Two(One):
 pass

 def second_class(self, add):
  One.add_access(self, add) 

