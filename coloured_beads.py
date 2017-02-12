#  d e p e n d e n c i e s
from termcolor import colored
from random import sample


#  c l a s s e s
class Bead():
    def __init__(self, color='white'):
        self.color = color
        self.symbol = '.'

    def draw(self):
        print colored(self.symbol, self.color, 'on_%s' % self.color)

class BigBead(Bead):
    def __init__(self, color='white'):
        Bead.__init__(self, color)
        self.symbol = '..'

class Box():
    def __init__(self):
        self.beads = []

    def count(self):
        return len(self.beads)

    def add(self, bead, k=1):
        for i in xrange(k):
            self.beads.append(bead)

    def remove(self, k=1):
        beads = sample(self.beads, k)
        for bead in beads:
            self.beads.pop(self.beads.index(bead))

        return beads


#  m a i n   e x e c u t i o n
B = Box()

B.add(Bead('white'), 70)
B.add(Bead('cyan') , 35)
B.add(Bead('yellow'), 35)
B.add(Bead('red'), 35)

B.add(BigBead('cyan'), 10)
B.add(BigBead('yellow'), 8)
B.add(BigBead('red'), 6)
B.add(BigBead('white'), 5)
B.add(BigBead('magenta'), 4)
B.add(BigBead('green'), 2)

for b in B.remove(B.count()):
    b.draw()
