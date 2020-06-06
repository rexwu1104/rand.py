from time_py import latency as l #導入上述的延遲函式

seed_out = int(l() * 10000) #讓它放大一萬倍，較好得到整數

def random(times : int): #亂數函式
  seed = seed_out #取得上面的變數
  for i in range(times): #執行times次
    seed = (seed * (2 ** 127 - 1) // int(l() * 10000)) % 65536 #產生偽亂數
    yield seed #回傳

