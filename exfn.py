print('\033[1;31mFunção de Notas:\033[m')

def notas(*n, sit=False):
    """
    -> Funcao para analisar notas e situacoes de varios alunos.
    n: uma ou mais notas dos alunos (aceita varias)
    sit: valor opcional, indicando se deve ou nao adicionar a situaçao
    return: dicionario com varias informacoes sobre a situacao da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 6:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

# Programa Principal
print('\033[1;31mExplicação:\033[m')
help(notas)
resp = notas(5.5, 2.5, 1.5, sit=True)
print('\033[1;31mResposta das notas 5.5, 2.5 e 1.5:\033[m')
print(resp)
print('\033[1;32mTérmino!\033[m')
