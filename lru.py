import collections
from collections import OrderedDict

class LRU:
  
  def __init__(self, capacity: int):
    self._capacity = capacity
    self.map = OrderedDict()

  
  def get(self, key: int) -> int:
    if key in self.map:
      value = self.map.pop(key)
      self.map[key] = value
      return value
    
    return -1

  
  def put(self, key: int, value: int) -> None:
    if key in self.map:
      self.map.pop(key)
    elif len(self.map) == self._capacity:
      self.map.popitem(last=False)
    
    self.map[key] = value