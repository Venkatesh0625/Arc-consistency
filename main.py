from CSProblem import CSProblem

arcs = [('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'b'), ('c', 'a'), ('a', 'c')]

domains = {
        'a': [2, 3, 4, 5, 6, 7],
        'b': [4, 5, 6, 7, 8, 9],
        'c': [1, 2, 3, 4, 5]
    }

constraints = {
        ('a', 'b'): lambda a, b: a * 2 == b,
        ('b', 'a'): lambda b, a: b == 2 * a,
        ('a', 'c'): lambda a, c: a == c,
        ('c', 'a'): lambda c, a: c == a,
        ('b', 'c'): lambda b, c: b >= c - 2,
        ('b', 'c'): lambda b, c: b <= c + 2,
        ('c', 'b'): lambda c, b: b >= c - 2,
        ('c', 'b'): lambda c, b: b <= c + 2
    }


problem = CSProblem(arcs, domains, constraints)
r = problem.arc_consistency()  

