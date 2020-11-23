import csv
import numpy as np

class ADUObj:
    def __init__(self,csvfilename):
        data = []
        with open(csvfilename,'r') as f:
            for row in csv.DictReader(f):
                data.append(row)

        keys = ('latitude','longitude',('time(millisecond)','t(ms)'),('height_above_takeoff(feet)','HAT(feet)'))
        for k in keys:
            if isinstance(k,tuple):
                setattr(self,k[1],np.array([f[k[0]] for f in data]))
            else:
                setattr(self,k,np.array([f[k] for f in data]))


