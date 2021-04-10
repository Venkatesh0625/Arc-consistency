from queue import Queue

class CSProblem:
    arc_queue = Queue()

    def __init__(self, arcs: list, domains: dict, constraints: dict):
        self.arcs = arcs
        self.domains = domains
        self.constraints = constraints

    def arc_consistency(self):

        for arc in self.arcs:
            self.arc_queue.put(arc)

        while not self.arc_queue.empty():
            x, y = self.arc_queue.get()

            if revise(x, y):
                if len(self.domains(x)) == 0:
                    return False

                [self.arc_queue.put(arc) for arc in self.arcs if arc[0] == y] 
        
        return True

    def revise(x, y):
        change = False 
        xdomain = self.domains[x]
        
        for a in xdomain[:]:
            if seek_support(x, y, a) == None:
                self.domains[x].remove(a)
                change = True 
        
        return change

    def seek_support31(x, y, a):
        b = 

    