s = [64, 89, 100, 85, 77, 58, 79, 67, 96, 87,
         87, 36, 82, 98, 84, 76, 63, 69, 53, 22]

count_su = 0            # 90점 ~ 100점
count_woo = 0           # 80점 ~ 89점
count_mi = 0            # 70점 ~ 79점
count_yang = 0          # 60점 ~ 69점
count_ga = 0            # 0점  ~ 59점

i = 0
while i < len(s) :
    if s[i] >= 90 and s[i] <=100 :
        count_su = count_su + 1
        
    if s[i] >= 80 and s[i] <= 89 :
        count_woo = count_woo + 1

    if s[i] >= 70 and s[i] <= 79 :
        count_mi = count_mi + 1

    if s[i] >= 60 and s[i] <= 69 :
        count_yang = count_yang + 1

    if s[i] >= 0 and s[i] <= 59 :
        count_ga = count_ga + 1

    i += 1
    
print('수 : %d명' % count_su)
print('우 : %d명' % count_woo)
print('미 : %d명' % count_mi)
print('양 : %d명' % count_yang)
print('가 : %d명' % count_ga)