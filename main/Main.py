from controller.GestaoAlunosController import GestaoAlunosController
# O sistema deverá permitir a Criação, Atualização, Remoção e Exibição do(s) Aluno(s).

def main():
    gestaoAlunos= GestaoAlunosController()

    gestaoAlunos.menu()


if __name__ == '__main__':
    main()
