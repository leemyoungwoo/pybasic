def get_list(list_data) :
    import csv
    f = open('population_2020.csv','r',encoding='utf-8')
    lines = csv.reader(f)
    
    header = next(lines)
    
    list_tmp = []
    for line in lines :
        list_tmp.append(line[:])
        
    for j in range(7) : 
        tmp = []
        for i in range(len(list_tmp)) :
            tmp.append(list_tmp[i][j])
        list_data.append(tmp)