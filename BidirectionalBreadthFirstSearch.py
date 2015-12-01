# DOESN'T ALWAYS WORK
def bidirectionalBFS(g,s,e):
    l = [[s]]
    r = [[e]]
    visited = set()
    while l and r:
        lpath = l.pop(0)
        rpath = r.pop(0)
        vl = lpath[-1]
        vr = rpath[-1]
        if vl == vr:
            rpath.reverse()
            return lpath + rpath[1:]
        else:
            if vl not in visited:
                for node in g[vl]:                    
                    l.append(lpath + [node])
                    if node == e:
                        return l[-1]
                visited.add(vl)
            if vr not in visited:
                for node in g[vr]:
                    r.append(rpath + [node])
                    if node == s:
                        X = r[-1]
                        X.reverse()
                        
                        return X
                visited.add(vr)
        
#WORKS FAST!
def bidirectionalBFScount(g,s,e):
    newl = set([s])
    newr = set([e])
    l,r = 1,1
    visited = set()
    while newl and newr:

        if newl.intersection(newr):
            return l+r-1
        else:
            newnewl = set()
            for vl in newl:
                if vl not in visited:
                    for node in g[vl]: 
                        if node == e:
                            return l+1
                        newnewl.add(node) 
                    visited.add(vl)
            newl = newnewl            
            l+=1
            if newl.intersection(newr):
                return l+r-1
            newnewr = set()
            for vr in newr:
                if vr not in visited:
                    for node in g[vr]:
                        if node == s:
                            return r+1
                        newnewr.add(node) 
                    visited.add(vr)
            newr = newnewr
            r+=1  
