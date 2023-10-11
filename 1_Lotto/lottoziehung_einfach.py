import random

def lotto_ziehung():
    #liste mit allen zahlen von 1 bis 45
    alle_zahlen = list(range(1, 46))
    
    #6 zahlen aus der liste ziehen
    gezogene_zahlen = random.sample(alle_zahlen, 6)
    
    return gezogene_zahlen

gezogene_zahlen = lotto_ziehung()
print(gezogene_zahlen)
