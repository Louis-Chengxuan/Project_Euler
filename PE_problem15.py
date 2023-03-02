# <Method1> (think by meself)
def grid():
    New_list = []
    list = ["2","3","4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20","21"]
    len_list = len(list)
    for m in range(0,len_list -1):
        New_list = []
        for i in range (1,len_list -m):
            if i ==1:
                num = 2*int(list[i])
                New_list.append(num)
            else:
                num = num + int(list[i])
                New_list.append(num)
        list = New_list
    return list
grid()

#binomial coefficients 
#for 20 x 20 gird. have to take 40 steps. 20 right and 20 down. choose 20 from 40. 40!/20!*(40-20)!


