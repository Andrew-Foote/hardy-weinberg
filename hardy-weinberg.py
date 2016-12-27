import enum
import random
from matplotlib import pyplot

class Allele(enum.Enum):
    DOMINANT = 'A'
    RECESSIVE = 'a'

HOMOZYGOUS_DOMINANT = frozenset((Allele.DOMINANT,) * 2)
HETEROZYGOUS = frozenset((Allele.DOMINANT, Allele.RECESSIVE))
HOMOZYGOUS_RECESSIVE = frozenset((Allele.RECESSIVE,) * 2)

class Organism:
    def __init__(self, alleles):
        self.alleles = frozenset(alleles)

    def ploidy(self):
        return len(self.alleles)

    def random_gamete(self):
        return random.choice(tuple(self.alleles))

def run(t, ifdict):
    population = []
    for alleles in ifdict:
        population.extend(Organism(alleles) for i in range(ifdict[alleles]))
    fdictrecord = []
    for i in range(t):
        #print("Generation", i)
        fdict = dict(zip((HOMOZYGOUS_DOMINANT, HETEROZYGOUS, HOMOZYGOUS_RECESSIVE), (0,) * 3))
        fdictrecord.append(fdict)
        for organism in population:
            fdict[organism.alleles] += 1
        #print("Frequency of AA:", fdict[HOMOZYGOUS_DOMINANT])
        #print("Frequency of Aa:", fdict[HETEROZYGOUS])
        #print("Frequency of aa:", fdict[HOMOZYGOUS_RECESSIVE])
        new_population = [Organism((organism.random_gamete(), random.choice(population).random_gamete())) for organism in population]
        population = new_population
    pyplot.plot(tuple(fdictrecord[i][HOMOZYGOUS_DOMINANT] for i in range(t)), c = 'red')
    pyplot.plot(tuple(fdictrecord[i][HETEROZYGOUS] for i in range(t)), c = 'green')
    pyplot.plot(tuple(fdictrecord[i][HOMOZYGOUS_RECESSIVE] for i in range(t)), c = 'blue')
    pyplot.xlabel('Generation')
    pyplot.ylabel('Frequency')
    pyplot.ylim((0, sum(ifdict.values())))
