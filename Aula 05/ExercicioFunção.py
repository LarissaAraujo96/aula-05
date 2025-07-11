#1 Que conte do numero 0 até o nuemro 10
#2 Que conte do um ao dez pulando de dois em dois
#3 Que de boa noite a uma lista de alunos

def zero_dez ():
    for i in range (11):
        print(i)

def pulando ():
    for i in range (0,11,2):
         print(i)

alunosList = ["Larissa", "Maju","Flora", "Thomaz", "Miah", "Penny"]
def boaNoite_Alunos ():
    for i in alunosList:
        print(f'Boa noite {i}')

zero_dez()
print("="*15)
pulando()
print("="*15)
boaNoite_Alunos()
print("="*15)
