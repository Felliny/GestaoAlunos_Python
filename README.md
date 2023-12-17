## Gestão de Alunos

Crie um sistema para gestão de Alunos  
  
O sistema deverá permitir a Criação, Atualização, Remoção e Exibição do(s) Aluno(s).  
A classe Aluno deve conter as seguintes características e comportamentos.  
  

Características :

- id 
  
- nascimento 
    
- ra 
    
- nome 
    

Comportamentos :

-  __str__    // Deve retornar um texto com os dados do aluno
    

Crie uma classe chamada ``GestaoAlunos``, contendo as seguintes características e comportamentos.  
  
Características:

- índice : int      // Indica em qual posição deve ser guardada a próxima instância de aluno
    
- alunos : Aluno[]  // lista
    

Comportamentos:

-  criar()
    
-  atualizar()  
    
-  excluir()  
    
-  exibir()  
    
-  menu()  
    

  
Regras do sistema

1. O comportamento criar() deve criar uma nova instância de Aluno, preencher as características desta instância com informações fornecidas pelo usuário, e deve guardar esta instância de aluno na matriz (alunos) na posição indicada pela variável índice.
2. A função exibir() deve pedir ao usuário para que digite um número de RA e procure qual aluno na matriz (alunos) possui um RA idêntico. Os dados do aluno encontrado devem ser exibidos na tela.
3. A função excluir() deve pedir ao usuário para digitar um RA, e em seguida deve excluir o(s) aluno(s) com este RA da matriz (alunos)
4. A função atualizar() deve pedir ao usuário para digitar um RA, e em seguida deve procurar pelo primeiro aluno na matriz (alunos) que contenha este RA. A função deve  em seguida solicitar ao usuário para que digite os demais dados do aluno (nome e nascimento) para trocar os valores das características do aluno encontrado na matriz pelos valores recém informados pelo usuário.
5. O método menu() deve rodar em um _loop_ infinito, mostrando na tela as opções para o usuário:

                (C)riar           (E)xibir             (R)emover                 
                (A)tualizar    (S)air

  

               Pegue a primeira letra digitada pelo usuário e assuma como sendo a opção escolhida
               Conforme a opção escolhida o método deve invocar a função correspondente criar(), exibir(), excluir(), atualizar() ou System.exit(0) para sair do sistema.
