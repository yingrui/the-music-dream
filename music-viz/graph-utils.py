from music21 import corpus, graph

aStream = corpus.parse('bach/bwv57.8')

# aStream.show('musicxml', '/Applications/Finale Notepad 2012.app')

graph.plotStream(aStream)

graph.plotStream(aStream, 'PlotHistogramPitchClass')

graph.plotStream(aStream, format='scatter', values=['pitch'])

# graph.plotStream(aStream, format='scatterweighted', values='pitchclass')

plot = graph.PlotDolan(aStream)
plot.process()