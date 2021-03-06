from tika import parser # pip install tika

raw = parser.from_file('edital.pdf')

x = raw['content']

tabela = x.split("Condutor:")

print(len(tabela))

i = 1

f = open("cnh_ms.txt", "a")

while (i < len(tabela)):
    linhas_tabela = tabela[i].splitlines()
    nome = linhas_tabela[0].lstrip()
    j = 0
    while ("Cnh" not in linhas_tabela[j]):
        j = j+1
    cnh = linhas_tabela[j].split(" ")[1]
    f.write(cnh)
    f.write("\n")
    print(nome)
    print(cnh)
    i = i+1

f.close()