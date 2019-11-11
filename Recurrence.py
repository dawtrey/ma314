def rec(i):
  if i == 1: return 1
  return rec(i-1) + rec(i // 2) 

print(rec(100))
