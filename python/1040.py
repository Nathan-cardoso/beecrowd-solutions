n1, n2, n3, n4 = map(float, input().split())

media = ((n1 * 2) + (n2 * 3 )+ (n3 * 4) + (n4 * 1))/10

print('Media: {:.1f}'.format(media))

if media >= 7.0:
    print('Aluno aprovado.')

elif media >= 5.0 and media < 6.9:
    print('Aluno em exame.')
    #print('Nota do exame: ', end='')
    notaExame = float(input('Nota do exame: '))
    mediafinal = (notaExame + media)/2
    if mediafinal >= 5.0:
        print('Aluno aprovado.')
    elif mediafinal < 5.0:
        print('Aluno reprovado.')
    
    print('Media final: {:.1f}'.format(mediafinal))

else:
    print('Aluno reprovado.')