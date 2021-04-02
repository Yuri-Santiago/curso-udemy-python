"""
10 - Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12,
e se o dia existe naquele mês. Note que Fevereito tem 29 dias em anos bissextos, e 28 dias em anos não bissesxtos.
"""

print('Digite uma data no formato "DD/MM/AAAA".')
data = input('Data: ')
data = data.split('/')

dia, mes, ano = data
dia = int(dia)
mes = int(mes)
ano = int(ano)

if ano < 2022:
    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    if bissexto:
        meses = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    else:
        meses = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if mes in meses:
        if dia > meses[mes] or dia < 1:
            print('Dia inválido')
        else:
            print('Data válida!')
    else:
        print('Mês inválido')
else:
    print('Ano inválido')
