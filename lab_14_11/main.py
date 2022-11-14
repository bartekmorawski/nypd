def create_file(name, line_count):
    f = open(name, 'w', encoding='utf-8')
    for i in range(line_count):
        f.write("line no. " + str(i+1) + "\n")
    f.close()

def count_lines(name):
    f = open(name, 'r')
    linie = 0
    for i in f:
        linie+=1
    f.close()
    return linie

def lines(name):
    f = open(name, 'r')
    lista = []
    for i in f:
        lista = lista + [i.rstrip()]
    f.close()
    return lista

def reversed_lines(input_name, output_name):
    f = open(input_name, 'r')
    g = open(output_name, 'w', encoding='utf-8')
    for i in f:
        odwr = i.rstrip()
        odwr = odwr [::-1]
        odwr = odwr + "\n"
        g.write(odwr)
    f.close()
    g.close()

def words(name):
    f = open(name, 'r')
    lista=[]
    for i in f:
        for j in i.split():
            lista += [j]
    f.close()
    return lista

def reversed_words_order(input_name, output_name):
    f = open(input_name, 'r')
    g = open(output_name, 'w', encoding='utf-8')
    for i in f:
        for j in i.split() [::-1]:
            g.write(j + " ")
        g.write("\n")
    f.close()
    g.close()

#ostatniego ze słownikiem nie robię bo nie umiem

create_file("example_14_11.txt", 5)
f = open("example_14_11.txt", "r")
print(f.read())
f.close()
print(count_lines("example_14_11.txt"))
print(lines("example_14_11.txt"))
reversed_lines("example_14_11.txt", "odwr_ex_14_11.txt")
f = open("odwr_ex_14_11.txt", "r")
print(f.read())
f.close()
print(lines("odwr_ex_14_11.txt"))
print(words("example_14_11.txt"))
reversed_words_order("example_14_11.txt", "odwr_slowa_ex_14_11.txt")
f = open("odwr_slowa_ex_14_11.txt", "r")
print(f.read())
f.close()