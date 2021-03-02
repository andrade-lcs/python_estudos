date = input('Entre com uma data aa/mm/aaaa:')
if '-' in date:
    date = date.replace('-', '/')
date = date.split('/')
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro')


if len(date[2]) <= 2:
    if int(date[2]) > 50:
        ano = int(date[2]) + 1900
    else:
        ano = int(date[2]) + 2000
else:
    ano = date[2]

print(f'Sua data é {date[0]} de {meses[(int(date[1]) - 1)]} de {ano}')
date_format = f'{date[0]}/{meses[(int(date[1]) - 1)]}/{ano}'
print(date_format)