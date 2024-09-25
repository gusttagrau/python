import os

arquivo_original = input("digite o nome do arquivo que sera renomeado")
novo_arquivo = input("digite o nome do novo arquivo")

mudarNome(arquivo_original, novo_arquivo)

# para criar uma funcao em python iremos utilizar o comando
# def(definicao)
def mudarnome(ar_or,nv_ar):
    """
    A funcao mudarnome, alterar o nome do arquivo.
    que o usuario deve passar o nome original do arquivo e
    o novo nome.
    Args:
        ar_or(str): O nome original do arquivo
        nv_ar(str): O novo nome do arquivo
    returns:
        retorna uma msg de confirmacao    
    """
    os.rename(ar_or,nv_ar)
    msg="o nome do arquivo foi alterado"
    return msg

arquivo_original= input("digite o nome do arquivo que sera renomeado")
novo_arquivo= input("digite o novo nome do arquivo")

rs = mudarnome(arquivo_original, novo_arquivo)
print(rs)
