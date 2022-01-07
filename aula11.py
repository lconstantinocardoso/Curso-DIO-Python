
lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read(
    divisao = 10 / 1
    numero = lista[1]

except ZeroDivisionError:
    print('Não é possível realizar uma divsão por 0')
except ArithmeticError:
    print('houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um erro inválido da lista')
except Exception as ex:
    print('Errro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
