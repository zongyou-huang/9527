# 井1標題9527
## 井2二標主軸

甚麼都沒有就內文

* 星號條列式
* 再弄一次
y=0
for x in range(1,101,2):
    y+=x
print('1~100中的所有奇數和:',y)


total=0
for i in range(1,10):
    for j in range (1,10):
        total=i*j
        print(i,'x',j,'=',total,'\n')
#老師不好意思，不換行列印學生看不舒服


t_score=0
t_student=0
t_pass=0
t_fail=0

while True:
    score=float(input('請輸入學生成績，輸入-1結束輸入'))
    if score == -1:
        break
    if score < -2:
        print('第',t_student+1,'位學生成績輸入錯誤，請重新輸入')
        continue
    
    t_student+=1
    t_score+=score
    
    if score >= 60:
        t_pass+=1
    else:
        t_fail+=1

print('全班人數為',t_student,'  ','及格人數為',t_pass,'  ','不及格人數為',t_fail,'  ','全班平均為',t_score/t_student)



for i in range (1,int(float(input("輸入星星金字塔高度上限:")))+1):
    print("*" * i)



for i in range (int(float(input("輸入星星倒金字塔高度上限:")))+1,0,-1):
    print("*" * i)



max_star=int(float(input('請輸入星星最長數量(奇數限定)')))
if max_star % 2 = 0L:
    print('請從頭輸入奇數')
    break
