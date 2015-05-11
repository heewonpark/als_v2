
NHOST = 4
CORE  = [[] for _ in range(NHOST)]

NPN = 1
NLN = 2
NRN = 10
NCELL = NPN+NLN+NRN

PN = "PN"
LN = "LN"
RN = "RN"


for pcid in range(NHOST):
    for i in range(NCELL):
        if  (i%NHOST==pcid)&(i<NPN):
            CORE[pcid].append(PN)
        elif(i%NHOST==pcid)&(i<NPN+NLN):
            CORE[pcid].append(LN)
        elif (i>=NPN+NLN):
            if(NHOST>NPN+NLN):
                if((i-NLN-NPN)%(NHOST-NPN-NLN))==(pcid-NPN-NLN):
                    print i
                    CORE[pcid].append(RN)                    
            else:
                if(i%NHOST==pcid)&(i>=NPN+NLN):
                    CORE[pcid].append(RN)                    

for j in range(NHOST):     
    print CORE[j]

pn=0
ln=0
rn=0

for i in CORE:
    for j in i:
        if(j=="PN"):
            pn+=1
        elif(j=="LN"):
            ln+=1
        elif(j=="RN"):
            rn+=1

print pn, ln, rn
