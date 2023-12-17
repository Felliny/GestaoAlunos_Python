from model.Aluno import Aluno


class GestaoAlunosController:
    indice = 0
    alunos = []

    def criar(self):
        aluno = Aluno()

        aluno.set_nome(input('Nome do aluno: '))
        aluno.set_ra(input('RA do aluno: '))
        aluno.set_nascimento(input('Data de nascimento: '))
        aluno.id = self.indice

        self.alunos.append(aluno)
        self.indice += 1

    def atualizar(self):
        ra = input('RA do aluno: ')

        for aluno in self.alunos:
            if aluno.ra == ra:
                aluno.nome = input('Nome do aluno: ')
                aluno.nascimento = input('Data de nascimento: ')

    def deletar(self):
        ra = input('RA do aluno: ')

        for aluno in self.alunos:
            if aluno.ra == ra:
                self.alunos.remove(aluno)

    def exibir(self):
        ra = input('RA do aluno: ')

        for aluno in self.alunos:
            if aluno.ra == ra:
                print(aluno.__str__())

    def menu(self):
        letra = ''

        while letra != 's':
            escolha = input("MENU \n (C)riar \n (E)xibir \n (R)emover \n (A)tualizar \n (S)air \n\n Escolha: ")
            letra = escolha[0].lower()

            if letra == 'c':
                self.criar()
            elif letra == 'e':
                self.exibir()
            elif letra == 'r':
                self.deletar()
            elif letra == 'a':
                self.atualizar()
