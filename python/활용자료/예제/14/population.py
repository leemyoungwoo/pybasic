def get_list(list_data) :
    import csv
    f = open('population_2020.csv', 'r', encoding='utf-8')
    lines = csv.reader(f)

    header = next(lines)
               
    list_tmp = []
    for line in lines :                       # CSV 버퍼의 내용을 리스트에 저장
        list_tmp.append(line[:])
        
    for j in range(7) :                       # 리스트의  행과 열을 변경
        tmp = []
        for i in range(len(list_tmp)) :     
            tmp.append(list_tmp[i][j])
        list_data.append(tmp)

def get_dict(list_data, keys, dict_data) :
    area = get_area(list_data[0])
    dict_data.update({keys[0]:area})

    for i in range(1, 7) :
        if i==3 or i==6 : 
            data = del_comma(list_data[i], 'float')
        else :
            data = del_comma(list_data[i], 'integer')
    
        dict_data.update({keys[i]:data})

def get_area(data) :            
    tmp = []
    for x in data :                      
        arr = x.split()             
        tmp.append(arr[0])
        
    return tmp

def del_comma(data, t) :
    tmp = []
    for x in data :
        string = ''
        arr = x.split(',')
        for i in range(len(arr)) :
            string += arr[i]
        
        if t == 'integer' :
            tmp.append(int(string))
        else :
            tmp.append(float(string))
        
    return tmp

