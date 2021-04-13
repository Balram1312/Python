# Given the names and grades for each student in a class of N students, store them in a nested list and print the
# name(s) of any student(s) having the second lowest grade.
if __name__ == '__main__':
    sheet = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        sheet.append([name, score])

    temp = sorted([marks for name, marks in sheet],reverse=True) # Get descending list of scores in sheet list
    for i in range(len(temp)):
        if i<len(temp)-1:
            if temp[i] > temp[i+1]:
                ans = temp[i]
    sheet = sorted([x for x , r in sheet if r == ans]) # Storing the names in sheet list who is second lowest in class
    for i in range(len(sheet)): # print output names in separate lines
        print(sheet[i])
