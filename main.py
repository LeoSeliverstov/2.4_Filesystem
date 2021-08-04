import os.path

dirs_list = []  # подходящие директории будем хранить в списке
os.chdir("main")  # из папки с проектом переходим в папку main, которая лежит здесь же

for current_dir, dirs, files in os.walk("."):
    for f in files:
        if f.endswith('.py') and (current_dir[2:] not in dirs_list):
            dirs_list.append(current_dir[2:])
# [2:] нужно потому, что программа дописывает ./ в начале пути к папке, а по условиям задачи нам это не нужно
# current_dir[2:] должно быть одинаковым в условии сравнивания и во внесении в список

sorted(dirs_list)  # сортируем список в лексикографическом порядке

file = open('result.txt', 'w')
for i in range(len(dirs_list)):
    file.write(dirs_list[i] + '\n')
file.close()
