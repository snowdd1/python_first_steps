import re
class Xdict(dict):
    '''
    # extended dict for deep access
    supports "dotted" notation for access to deeper levels, supporting both dict and list subtypes.
    ``xdict = Xdict(dict)`` Constructor, returns a Xdict.
    ``xdict[pathlist]``:
    ``xdict[['dot.notation.getitem', 'alternative.path']]`` returns the value of getitem in a dictionary of the structure {'dot': {'notation': {'getitem':42}}}, 'alternative.path' will only by tried if 'dot.notation.getitem' is not a valid path.
    ``xdict.dot.notation.getitem`` will also return the famous 42 here for dict-only deep structures.
    ``xdict['dot']``  same as dict['dot']
    ``xdict.verbose=True`` enable print outs for debugging. 
    '''
    def __dotfind(data, path):
        data = data.copy()
        # ignore escaped dots
        pescaped = re.sub('\r', '.', re.sub('\.', '\n', re.sub('\\\.', '\r', path),),)
        for p in pescaped.split('\n'):
            try:
                if isinstance(data, (tuple, list)):
                    p2 = int(p)
                elif isinstance(data, dict):
                    p2 = p
                data = data[p2]
            except:
                raise
        return data
    def __init__(self, *args, **kwargs):
        super(Xdict, self).__init__(*args, **kwargs)
        self.verbose = False
    def __getattr__(self,name):
        try:
            z = self[name]
            if self.verbose:
                print('Name: ', name, ' Type: ', type(name))
            if isinstance(z, dict):
                return Xdict(z)
            else:
                return z
        except:
            pass
    def __getitem__(self, paths):  
        if isinstance(paths, list):
            for path in paths:  
                if self.verbose:
                    print(path, end=':')
                try:  
                    val = self.__dotfind(path)  
                    if self.verbose:
                        print('Success, value =',val)
                    break  
                except KeyError: 
                    if self.verbose:
                        print('Error')
                    pass # log it but no handling needed  
            else:  
                val = None # handle not found  
            return val 
        else:
            return super(Xdict, self).__getitem__(paths)

class Xlist(list):
    def __dotfind(data, path):
        data = data.copy()
        # ignore escaped dots
        pescaped = re.sub('\r', '.', re.sub('\.', '\n', re.sub('\\\.', '\r', path),),)
        for p in pescaped.split('\n'):
            try:
                if isinstance(data, (tuple, list)):
                    p2 = int(p)
                elif isinstance(data, dict):
                    p2 = p
                data = data[p2]
            except:
                raise
        return data
    def __init__(self, *args, **kwargs):
        super(Xdict, self).__init__(*args, **kwargs)
        self.verbose = False
    def __getattr__(self,name):
        try:
            z = self[name]
            if self.verbose:
                print('Name: ', name, ' Type: ', type(name))
            if isinstance(z, dict):
                return Xdict(z)
            else:
                return z
        except:
            pass