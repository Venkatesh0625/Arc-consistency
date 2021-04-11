from queue import Queue
from collections import defaultdict

class CSProblem:
    arc_queue = Queue()

    def __init__(self, arcs: list, domains: dict, constraints: dict):
        self.arcs = arcs
        self.domains = domains
        self.constraints = constraints
        self.residue = {arc: {x: None for x in self.domains[arc[0]]} for arc in self.arcs} 

    def arc_consistency(self):

        for arc in self.arcs:
            self.arc_queue.put(arc)

        while not self.arc_queue.empty():
            
            x, y = self.arc_queue.get()
    
            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    yield None 
                    break

                neighbours = [arc for arc in self.arcs if arc[0] == y]
                [self.arc_queue.put(arc) for arc in neighbours] 

                yield ((x, y), self.domains, neighbours)
            else:
                yield((x, y), self.domains, None)
        
        yield(None, self.domains, None)

    def revise(self, x, y):
        change = False 
        xdomain = self.domains[x]
        
        for a in xdomain[:]:
            t = self.seek_support((x, y), a)
            if t == None:
                self.domains[x].remove(a)
                change = True 
        
        return change

    def seek_support(self, arc, a):
        x, y = arc
        xdomain = self.domains[x]
        ydomain = self.domains[y]

        checker = self.constraints[arc]

        if self.residue[arc][a] in ydomain:
            return self.residue[arc][a]

        beg = self.beginning(arc, a)
        if beg in ydomain:
            return beg

        end = self.end(arc, a)
        if end in ydomain:
            return end

        
        b = self.next(ydomain, beg)
        
        for _ in ydomain:
            if checker(a, b):
                self.residue[arc][a] = b
                self.residue[arc][b] = a
                return b
            else:
                b = self.next(ydomain, b)

        return b 

    def beginning(self, arc, a):
        x, y = arc
        checker = self.constraints[arc]

        for b in self.domains[y]:    
            if checker(a, b):
                return b
        return None

    def next(self, domain, a):
        if a == None:
            return domain[0]
            
        if a == domain[-1]:
            return None
        return domain[domain.index(a)+1]

    def end(self, arc, a):
        x, y = arc
        checker = self.constraints[arc]

        for b in reversed(self.domains[y]):
            if checker(a, b):
                return b
        return None

