s=input()
s.isdigit()
sum2=0
sum1=0
if s.isdigit():
    if len(s) == 16:
        for i in s[0:len(s):2]:
            if int(i) * 2 >=10 :
                sum2+= 2 * int(i)%10 + 2 * int(i)//10
            else:
                sum2+=int(i)*2
        for i in s[1:len(s):2]:
            sum1+=int(i)
        if (sum1+sum2)%10 == 0 and int(s)!=0:
            print("карта корректнм")
        else:
            print("карта некорректна")
            print(sum2)
    else:
        print("Карта неикорреткна")
else:
    print("ошибка")
