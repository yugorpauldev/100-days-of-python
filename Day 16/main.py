#
#timmy = Turtle()
#timmy.shape("turtle")
#timmy.color("coral")
#timmy.forward(100)
#my_screen = Screen()
#
# #print(my_screen.canvheight)
#
#my_screen.exitonclick()

from prettytable import PrettyTable

lista_nome = []
lista_tipo = []


def adicionar():
    decisao = True
    while decisao:
            nome = input("Insira o nome do Pockemon")
            lista_nome.append(nome)
            tipo = input("Insira o tipo do Pokemon")
            lista_tipo.append(tipo)

            escolha = input("Deseja adicionar um pokemon")

            if escolha == "y":
                decisao = True
            else:
                decisao = False

table = PrettyTable()
def create(lista, lista2):

    table.add_column("Pokemon name",
                     lista)
    table.add_column("Type",lista2)

    table.align = 'l'
    print(table)

print(lista_nome)
create(lista_nome,lista_tipo)