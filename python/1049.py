#Animal
def process_output(animals):

    if animals[0] == 'vertebrado' and animals[1] == 'ave' and animals[2] == 'carnivoro':
        return 'aguia'
    
    elif animals[0] == 'vertebrado' and animals[1] == 'ave' and animals[2] == 'onivoro':
        return 'pomba'
    
    elif animals[0] == 'vertebrado' and animals[1] == 'mamifero' and animals[2] == 'onivoro':
        return 'homem'
    
    elif animals[0] == 'vertebrado' and animals[1] == 'mamifero' and animals[2] == 'herbivoro':
        return 'vaca'
    
    elif animals[0] == 'invertebrado' and animals[1] == 'inseto' and animals[2] == 'hematofago':
        return 'pulga'
    
    elif animals[0] == 'invertebrado' and animals[1] == 'inseto' and animals[2] == 'herbivoro':
        return 'lagarta'
    
    elif animals[0] == 'invertebrado' and animals[1] == 'anelideo' and animals[2] == 'hematofago':
        return 'sanguessuga'
    
    elif animals[0] == 'invertebrado' and animals[1] == 'anelideo' and animals[2] == 'onivoro':
        return 'minhoca'
    

words = []

for i in range(0,3):
    words.append(str(input()).lower().strip())


print(process_output(words))

