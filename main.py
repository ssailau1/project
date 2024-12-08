class ReverseIterator:
 def __init__(self, reverse):
     self.i=0
     self.reverse = reverse
 def  __iter__(self):
     self.i=0
     return self
 def __next__(self):
     self.i = 0
     return self

ReverseIterator= [1, 2, 3, 4, 5]
iterator = iter(ReverseIterator)
ReverseIterator.reverse()

for ReverseIterator in ReverseIterator:
 print(ReverseIterator)