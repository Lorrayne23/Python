# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Livro():
    def __init__(self, nome, cidade, telefone,email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email


    def __len__(self):
            return self.telefone

    def __str__(self):
        return self.cidade



pessoa = Livro('Ana','Belo Horizonte',345966,'ana@gmail.com')
print(len(pessoa))
print(str(pessoa))
