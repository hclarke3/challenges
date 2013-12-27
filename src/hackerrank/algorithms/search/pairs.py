#!/usr/bin/py
# Head ends here
def pairs(a,k):
  #a contains array of numbers and k is the value of difference
  hm = {}
  answer = 0

  for i in a:
      hm[i] = -1

  for i in a:
      diff = i - k
      if (diff in hm):
          answer += 1

  return answer

# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)