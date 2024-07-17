def uniq (x , y ):
    file_path = 'all_Q.txt'
    line_numbers_to_read = list(range(x,y)) 
    specific_lines = read_specific_lines(file_path, line_numbers_to_read)
    return specific_lines
def vijegi():
    return uniq(73,81)[::-1]
def rolls():
    return uniq(64,72)
def read_specific_lines(filename, line_numbers):
  with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    selected_lines = [lines[i - 1].strip() for i in line_numbers]
  return selected_lines
def q ():
    return uniq(1,8)
def a_al():
       results = []
       start = 8
       end = 64
       while start < end:
           results.append(uniq(start, start + 8))
           start += 8
       return results
def check(arr):
    res = sum(arr)
    if res > 10 :
        v = True
    else:
        v = False
        
    return v    
        
def p_q (): 
    qous = q()
    qs_a = a_al()
    all_sce = []
    for i in range(len(qous)):
        points = []
        print(qous[i][::-1])
        for j in range(8):
            print(qs_a[i][j][::-1])
            txt_1 = "از یک تا ده امتیاز وارد کنید:"[::-1]
            print(txt_1)
            score = int(input(":  "))
            points.append(score)
        while check(points):
            for k in range(6):
                print(qs_a[i][k][::-1])
                print("\n")
            mssge = "امتیاز بیشتر از ده شده ؛ تعویض امتیاز کدام سوال؟"[::-1]
            print(mssge)
            change = int(input(" ")) - 1
            print(qs_a[i][change][::-1])
            new_s = int(input('?  '))
            points[change] = new_s
        all_sce.append(points)
    return all_sce        
            
def col_s(arr):
    c_1 = arr[0][6]+ arr[1][0] + arr[2][7]+ arr[3][3] +arr[4][1] +arr[5][5] +arr[6][4] 
    c_2 = arr[0][3]+ arr[1][1] + arr[2][0]+ arr[3][7] +arr[4][5] +arr[5][2] +arr[6][6]  
    c_3 = arr[0][5]+ arr[1][4] + arr[2][2]+ arr[3][1] +arr[4][3] +arr[5][6] +arr[6][0] 
    c_4 = arr[0][2]+ arr[1][6] + arr[2][3]+ arr[3][4] +arr[4][7] +arr[5][0] +arr[6][5] 
    c_5 = arr[0][0]+ arr[1][2] + arr[2][5]+ arr[3][6] +arr[4][4] +arr[5][7] +arr[6][3]
    c_6 = arr[0][7]+ arr[1][3] + arr[2][6]+ arr[3][2] +arr[4][0] +arr[5][4] +arr[6][1]           
    c_7 = arr[0][1]+ arr[1][5] + arr[2][4]+ arr[3][0] +arr[4][2] +arr[5][1] +arr[6][7]
    c_8 = arr[0][4]+ arr[1][7] + arr[2][1]+ arr[3][5] +arr[4][6] +arr[5][3] +arr[6][2]
    cs = [c_1 , c_2 , c_3 , c_4 , c_5 , c_6 ,c_7 , c_8]
    return cs        
def maximm(cs , all_sce):
    m = max(cs )
    awn = 0
    q = cs.count(m)
    t = "بهتر است تغییراتی ایجاد کنید"[::-1]
    ta = " کدام سوال را تغییر میدهید؟ "[::-1]
    ab = "سوال؟ "[::-1]  
    ac = "بخش؟"[::-1]  
    while q > 1 :
        print(t)
        print(ta)          
        print("\n")
        alll =a_al()
        print(alll[::-1])
        print(ab)           
        ch_q = int(input(" ?  "))
        print(ac)       
        ch_b= int(input(" ? "))
        new= int(input(" score  ? "))
        all_sce[ch_q-1][ch_b-1] = new
        cs = col_s(all_sce)
        m = max(cs )
        q = cs.count(m)
    for i in cs:
        if cs[i]== m:
            awn = i
            return awn 

    return awn
def result(numb ):
    rlls = rolls()
    vi = vijegi()
    txt_a = "گروه شما : "[::-1]
    txt_b = "ویزگی ها "[::-1]
    txt_c ="نقاط ضعف قابل تحمل"[::-1]
    txt_d = "مشوق ها "[::-1] 
    
    if numb == 0:
        print(txt_a)
        print('\n')
        print(rlls[0])
        print(txt_b)
        print('\n')
        print(vi[0])        
    elif numb == 1 :
        print(txt_a)
        print('\n')
        print(rlls[1])
        print(txt_b)
        print('\n')
        print(vi[1])
    elif numb== 2:
        print(txt_a)
        print('\n')
        print(rlls[2])
        print(txt_b)
        print('\n')
        print(vi[2])  
    elif numb == 3:
        print(txt_a)
        print('\n')
        print(rlls[3])
        print(txt_b)
        print('\n')
        print(vi[3])     
    elif numb == 4:
        print(txt_a)
        print('\n')
        print(rlls[4])
        print(txt_b)
        print('\n')
        print(vi[4])
    elif numb == 5:
        print(txt_a)
        print('\n')
        print(rlls[5])
        print(txt_b)
        print('\n')
        print(vi[5])                    
    elif numb == 6:
        print(txt_a)
        print('\n')
        print(rlls[6])
        print(txt_b)
        print('\n')
        print(vi[6])    
    elif numb == 7:
        print(txt_a)
        print('\n')
        print(rlls[7])
        print(txt_b)
        print('\n')
        print(vi[7])          
while True:
    txt = "برای شرکت در ازمون کلیک کنید:"[::-1]
    print(txt)
    choice = int(input(""))
    match choice:
        case 1 :
            a = p_q()   
            # print(a)
            b = col_s(a)
            print(b)
            m = max(b)
            print(m)
            c =  maximm(b , a)
            print(c)
            result(c)