import os
import random

def do_pliku(): #tworzy zapis do pliku
    output = 'Model; Output value; Time of computation; \n'
    output = output + random.choice(['A', 'B', 'C']) + ' ; ' + str(random.randint(0, 1000)) + ' ; ' + str(random.randint(0,1000)) + 's; '
    return output

def zrob_foldery_pliki(path_main): #tworzy podfoldery i pliki
    os.chdir(path_main)
    dni = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    pory = ['morning', 'evening']
    for i in dni:
        path = os.path.join(path_main, i)
        os.mkdir(path)
    for i in os.listdir(path_main):
        path = os.path.join(path_main, i)
        os.chdir(path)
        for j in pory:
            path2 = os.path.join(path, j)
            os.mkdir(path2)
            os.chdir(path2)
            f = open('Solutions.csv', 'w', encoding='utf-8')
            f.write(do_pliku())
            f.close()

def czas_z_pliku_A(sciezka): #daje czas z pliku jesli to A, jesli nie A to 0
    os.chdir(sciezka)
    f = open('Solutions.csv', 'r')
    linia = f.readlines()
    linia = linia[-1]
    linia = linia.split()
    if linia[0] == 'A':
        czas = int(linia[-1][:-2])
    else:
        czas = 0
    f.close()
    return czas

def sumuj_czasy(path_main): #dostajac sciezke i zakladajac strukture taka jak w zadaniu ale bez wiedzy o liczbie podfolderow sumuje czasy dla A
    suma = 0
    for i in os.listdir(path_main):
        path = os.path.join(path_main, i)
        for j in os.listdir(path):
            os.chdir(os.path.join(path, j))
            suma += czas_z_pliku_A(os.path.join(path, j))
    return suma

path_main = os.path.join(os.getcwd(), 'dni')
os.mkdir(path_main) #tworzy glowny folder
zrob_foldery_pliki(path_main) #tworzy w glownym folderze odpowiednie podfoldery i w nich takze a w tych pliki, zapisuje do plikow
print(sumuj_czasy(path_main)) #sumuje czasy dla A