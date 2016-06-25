from music21 import *

coreCorpus = corpus.corpora.CoreCorpus()

for path in coreCorpus.getPaths():
    print path