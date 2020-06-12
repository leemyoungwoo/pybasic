print('-' * 60) 
print('센티미터(cm) 인치(inch)   피트(ft)    야드(yd)')
print('-' * 60) 

for cm in range(10, 201, 10) : 
    inch = cm * 0.393701 
    ft = cm * 0.032808
    yd = cm * 0.010936
    print('%8d  %10.1f %10.1f  %10.1f' % (cm, inch, ft, yd))   
     
print('-' * 60)