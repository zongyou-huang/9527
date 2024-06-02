max_star=int(float(input('請輸入寬邊星星數量(奇數限定)')))
if max_star % 2 == 0:
  print('請重頭輸入奇數')
else:
  for i in range(max_star//2,0,-1):
    print(' '*i,'*'*(max_star-i*2))  #測試時一直跑出i+1個降冪的空白鍵，但個人覺得公式沒錯
  print('*'*max_star)
  for n in range(1,max_star//2+1):
    print(' '*n,'*'*(max_star-n*2))
