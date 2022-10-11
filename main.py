a=input()
if len(s)!=16
  print('ошибка')
else: 
  sum1=0
  for v in range(0, len(a),2):
      n=int(a[v])
      if n*2>9
          sum1=sum1(n*2-9)
      else:
          sum1=sum1+n*2
  sum2=0
  for z in range(1, len(s),2):
      m=int(s[z])
      sum2=sum2+m
  n=sum1+sum2
  if n%10==0:
      print('карта корректна')
  else:
    print('ошибка')
