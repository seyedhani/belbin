import os

def read_specific_lines(filename, line_numbers):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        selected_lines = [lines[i - 1].strip() for i in line_numbers]
    return selected_lines
def uniq(x, y):
    file_path = 'all_Q.txt'
    line_numbers_to_read = list(range(x, y))
    return read_specific_lines(file_path, line_numbers_to_read)

def vijegi():
    return uniq(73, 81)[::-1]

def rolls():
    return uniq(64, 72)

def q():
    return uniq(1, 8)

def a_al():
    results = []
    start = 8
    end = 64
    while start < end:
        results.append(uniq(start, start + 8))
        start += 8
    return results

def check(arr):
    return sum(arr) > 10

def p_q():
    main_questions = q()
    sub_questions = a_al()
    all_scores = []

    def get_scores_for_question(i):
        points = []
        print(main_questions[i][::-1])
        for j in range(8):
            print(sub_questions[i][j][::-1])
            prompt = "از یک تا ده امتیاز وارد کنید:"[::-1]
            print(prompt)
            score = int(input(":  "))
            points.append(score)
        return points

    for i in range(len(main_questions)):
        points = get_scores_for_question(i)
        while check(points):
            for k in range(6):
                print(sub_questions[i][k][::-1])
                print("\n")
            prompt = "امتیاز بیشتر از ده شده ؛ تعویض امتیاز کدام سوال؟"[::-1]
            print(prompt)
            change = int(input(" ")) - 1
            print(sub_questions[i][change][::-1])
            new_score = int(input('?  '))
            points[change] = new_score
        all_scores.append(points)
    return all_scores

def col_s(arr):
    columns = [
        [arr[0][6], arr[1][0], arr[2][7], arr[3][3], arr[4][1], arr[5][5], arr[6][4]],
        [arr[0][3], arr[1][1], arr[2][0], arr[3][7], arr[4][5], arr[5][2], arr[6][6]],
        [arr[0][5], arr[1][4], arr[2][2], arr[3][1], arr[4][3], arr[5][6], arr[6][0]],
        [arr[0][2], arr[1][6], arr[2][3], arr[3][4], arr[4][7], arr[5][0], arr[6][5]],
        [arr[0][0], arr[1][2], arr[2][5], arr[3][6], arr[4][4], arr[5][7], arr[6][3]],
        [arr[0][7], arr[1][3], arr[2][6], arr[3][2], arr[4][0], arr[5][4], arr[6][1]],
        [arr[0][1], arr[1][5], arr[2][4], arr[3][0], arr[4][2], arr[5][1], arr[6][7]],
        [arr[0][4], arr[1][7], arr[2][1], arr[3][5], arr[4][6], arr[5][3], arr[6][2]]
    ]
    return [sum(column) for column in columns]

def maximm(cs, all_scores):
    max_score = max(cs)
    t = "بهتر است تغییراتی ایجاد کنید"[::-1]
    ta = " کدام سوال را تغییر میدهید؟ "[::-1]
    ab = "سوال؟ "[::-1] 
    ac = "بخش؟"[::-1] 

    while cs.count(max_score) > 1:
        print(t)
        print(ta)         
        print("\n")
        all_questions = a_al()
        print(all_questions[::-1])
        print(ab)          
        ch_q = int(input(" ?  ")) - 1
        print(ac)      
        ch_b = int(input(" ? ")) - 1
        new_score = int(input(" score  ? "))
        all_scores[ch_q][ch_b] = new_score
        cs = col_s(all_scores)
        max_score = max(cs)
    return cs.index(max_score)

def result(numb):
    rlls = rolls()
    vi = vijegi()
    txt_a = "گروه شما : "[::-1]
    txt_b = "ویزگی ها "[::-1]
    if 0 <= numb < len(rlls):
        print(f"{txt_a}\n\n{rlls[numb]}\n{txt_b}\n\n{vi[numb]}")

def main():
    while True:
        txt = "برای شرکت در ازمون کلیک کنید:"[::-1]
        print(txt)
        choice = int(input(""))
        if choice == 1:
            all_scores = p_q()  
            column_scores = col_s(all_scores)
            print(column_scores)
            max_score = max(column_scores)
            print(max_score)
            result_index = maximm(column_scores, all_scores)               
            print(result_index)
            result(result_index)
if __name__ == "__main__":
    main()

            