import csv
# pst = post
# cmpt = compartment

class SYNLIST:
    def __init__(self):
        self.pre_gid      = -1
        self.pst_gid      = -1
        self.nconnections = -1
        self.pre_cmpts = []
        self.pst_cmpts = []

    def set_nconnections(self,nconnections):
        self.nconnections = nconnections

    def init_cmpts(self):
        self.pre_cmpts = [-1 for i in range(self.nconnections)]
        self.pst_cmpts = [-1 for i in range(self.nconnections)]

    def init_gids(self):
        self.gids = [-1 for i in range(self.nconnections)]

    def set_pregid(self,pregid):
        self.pre_gid = pregid
    
    def set_pstgid(self,pstgid):
        self.pst_gid = pstgid
        
    def set_precmpts(self,precmpts):
        self.pre_cmpts = precmpts

    def set_pstcmpts(self,pstcmpts):
        self.pst_cmpts = pstcmpts
        
    def get_precmpt(self,x):
        return self.pre_cmpts[x]

    def get_pstcmpt(self,x):
        return self.pst_cmpts[x]

    def set_gids(self,gids):
        self.gids = gids

    def set_gid(self,x,gid):
        self.gids[x] = gid

    def get_gid(self,x):
        return self.gids[x]

    def write_synlist(self,filename):
        print "\t%s"%(filename)
        self.ff = open(filename,'w')
        self.ff.write("$ PRE_CELL %d\n"%(self.pre_gid))
        self.ff.write("$ POST_CELL %d\n"%(self.pst_gid))
        self.ff.write("$ NCONNECTIONS %d\n"%(self.nconnections))
        for i in range(self.nconnections):
            self.ff.write("%d %d %d\n"%(self.get_precmpt(i),self.get_pstcmpt(i),self.get_gid(i)))
        self.ff.close()
    
    def read_synlist_format(self,pregid,pstgid,filename):
        print "read_synlist_format(%d,%d,%s)"%(pregid,pstgid,filename)
        self.set_pregid(pregid)
        self.set_pstgid(pstgid)
        fh = open(filename, 'r')
        reader = csv.reader(fh)
        synlist = [[] for _ in range(2)]
        for row in reader:
            self.pre_cmpts.append(row[0])
            self.pst_cmpts.append(row[1])
