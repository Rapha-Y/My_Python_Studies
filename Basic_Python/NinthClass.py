import shutil

def write_file(text):
    path = 'C:/Users/Anni/Documents/Projects/My_Python_Studies/teste.txt'
    file = open(path, 'w')
    file.write(text)
    file.close()

def update_file(file_name, text):
    file = open(file_name, 'a')
    file.write(text)
    file.close()

def read_file(file_name):
    file = open(file_name, 'r')
    text = file.read()
    print(text)

def mean_grades(file_name):

    file = open(file_name, 'r')
    std_grades = file.read()
    std_grades = std_grades.split("\n")

    mean_list = []

    for i in std_grades:
        grade_list = i.split(",")
        student = grade_list[0]
        grade_list.pop(0)
        mean = lambda grades: sum([int(j) for j in grades]) / 4
        mean_list.append({student:mean(grade_list)})

    return mean_list

def copy_file(file_name):
    shutil.copy(file_name, "C:/Users/Anni/Documents/Projects/notas_alunos.txt")

def move_file(file_name):
    shutil.move(file_name, "C:/Users/Anni/Documents/Projects")

if __name__ == '__main__':
    #write_file("First\nSecond")
    #student = "\nOkuyasu,2,2,2,1"
    #update_file("notas.txt", student)
    #read_file("teste.txt")
    mean_list = mean_grades("notas.txt")
    print(mean_list)
    #copy_file("notas.txt")
    #move_file("notas.txt")