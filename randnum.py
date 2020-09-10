import time
import random

class rand():
  def __l(self):
    before = time.time()
    for i in range(10000):
      continue

    after = time.time()
    return after - before

  def __init__(self, **kargs):
    self.num = []
    self.seed_out = int(self.__l() * 10000 * random.randint(1, 100))
    if "max" in kargs:
      self.max = kargs["max"]
    else:
      self.max = 65536
    if "min" in kargs:
      self.min = kargs["min"]
    else:
      self.min = 1
    if "deleted" in kargs:
      self.deleted = kargs["deleted"]
    else:
      self.deleted = []

  def rand(self, times : int):
    nummax = self.max - self.min
    nummin = 1
    self.num = [] + self.deleted
    seed = self.seed_out
    if times > nummax:
      limit = times // nummax 
      nums = times % nummax
    else:
      limit = 1
      nums = times
    for i in range(times):
      seed = (seed * (2 ** 127 - 1) // int(self.__l() * 10000 *random.randint(1, 100))) % nummax + nummin
      while True:
        if seed not in self.num and limit != 0:
          self.num.append(seed)
          break
        elif len(self.num) == nummax and limit != 0:
          limit -= 1
          self.num = [] + self.deleted
        elif limit == 0 and len(self.num) != nums and seed not in self.num:
          self.num.append(seed)
          break
        else:
          seed = seed * (2 ** int(self.__l() * 1000 *random.randint(1, 100))) * int(self.__l() * 10000 *random.randint(1, 100)) % nummax + nummin
      yield seed + self.min - 1
  
  def setup(self, max : int = 65536, min : int = 1, deleted : list = []):
    self.max = max
    self.min = min
    self.deleted = deleted
