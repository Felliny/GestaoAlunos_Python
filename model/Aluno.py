from datetime import datetime


class Aluno:
    id = None
    ra = None
    nome = None
    nascimento = None

    def get_id(self): return self.id

    def get_nascimento(self): return self.nascimento

    def get_ra(self): return self.ra

    def get_nome(self): return self.nome

    def set_id(self): self.id = id

    def set_nascimento(self, nascimento):
        data_formatada = datetime.strptime(nascimento, "%d/%m/%Y")  # Transfoma uma string em data
        self.nascimento = data_formatada.strftime("%d/%m/%Y")  # Transforma uma data em string

    def set_ra(self, ra): self.ra = ra

    def set_nome(self, nome): self.nome = nome

    def __str__(self):
        return f'id: {self.id} - Nascimento: {self.nascimento} - ra: {self.ra} - nome: {self.nome}'
