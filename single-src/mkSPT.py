import numpy as np
freq = 400
spt = np.linspace(6.010,7.010,num=freq,endpoint=False)+1/freq
np.savetxt("rn_spt%dHz.dat"%freq,spt,fmt='%.5f',comments='',footer='%d'%spt.size)
