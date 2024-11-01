import sys 

satisfaitVocab=['satisfait','content','excellent','bien','parfait','super','aimé','adoré','heureux','merci','satisfaisant','amélioré','remarquable','délicieux','satisfaite','accompli','recommand']
insatisfaitVocab=['insatisfait','désappointé','déçu','désagréable','mauvais','péché','pénible','nul','décevant','malheureux','manquant','absent','bof','incompetents']

for line in sys.stdin:
    line = line.strip()
    satisfait=False
    insatisfait=False
    for word in line.split():
        if word.lower() in satisfaitVocab:
            satisfait=True
        elif word.lower() in insatisfaitVocab:
            insatisfait=True
    if satisfait and not insatisfait:
        print('{}\t{}'.format('satisfait', 1)) 
    elif insatisfait and not satisfait:
        print('{}\t{}'.format('insatisfait', 1)) 
    elif satisfait and insatisfait:
        print('{}\t{}'.format('inconcluant', 1)) 

