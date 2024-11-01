import sys 
def readInput():
    input=[]
    for line in sys.stdin: 
        input.append(line.strip())  
    return input
def anagrammes(ch1,ch2):
        return sorted(ch1) == sorted(ch2)

def mapper(input=[]):
     ang=[]
     for word in input:
        if(not sorted(word) in ang):
            ang.append(sorted(word))
            myang=[word]
            for word2 in input:
                 if(word2!=word and anagrammes(word,word2)):
                      myang.append(word2)
            if(len(myang)>1):
                print('\t'.join(myang))
mapper(readInput())

