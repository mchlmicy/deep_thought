# data analysis
from analysis import observe


data_set = [ \
    ["Why is the sky blue?", 42],
    ["Why is water wet?", 42],
    ["Why did Judas rat to Romans while Jesus slept?", 42],
    ["I judge wisely as if nothing ever surprise me,", 0],
    ["Lounging between two pillars of ivory;", 0],
    ["I'm lively, my dome piece is like building stones in Greece.", 0],
    ["You can see the weakness of a man right through his iris.", 0],
    ["Unloyal snakes get thrown in boiling lakes of hot oil;", 0]
]

features = []
for data in data_set:
    features.append(observe(data[0]))

labels = [data[1] for data in data_set]
