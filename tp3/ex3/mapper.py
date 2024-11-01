import sys 
input=[]
pages=[]
for line in sys.stdin :
    input.append(line.strip().split(','))
for i in input :
    aux=i[0].split(':')
    i.remove(i[0])
    i=aux+i
    pages.append(i)

for page in pages :
    current_page=page[0]
    i_web_inv=[]
    for ipage in pages :
        if(ipage[0]!=current_page and ipage.__contains__(current_page)):
            i_web_inv.append(ipage[0])
        
    print(current_page + ': '+', '.join(i_web_inv))