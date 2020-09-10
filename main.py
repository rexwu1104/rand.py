from randnum import rand

gen = rand(max=1000, min=100)

for result in gen.rand(900):
  print(result)
