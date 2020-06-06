import time #導入時間套件

def latency(): #計算延遲的函式
  before = time.time() #動作前記錄時間
  for i in range(10000): #執行某個動作一百次
    continue

  after = time.time() #執行完後記錄
  return after - before #回傳出動作前後的延遲