# determine if a list is sorted

sorteditems = [1,2,6,78,98,99,123,145,157]
unsorteditems = [1,2,4,6,8,9,12,15,21,18,19,25,27]

def issorted(items):
    # for i in range(0,len(items)-1):
    #     if(items[i] > items[i+1] ):
    #         return False
    # return True
    return all(items[i] <= items[i+1] for i in range(len(items)-1))

print(sorteditems," is sorted? ",issorted(sorteditems),"\n")
print(unsorteditems," is sorted? ",issorted(unsorteditems))
