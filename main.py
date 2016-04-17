# analysis
from analysis import observe

# machine learning
from learn import classifier

# system
import sys


if len(sys.argv) >= 2:
    submission, text = sys.argv[1:], ''
    for statement in submission:
        text += ' ' + str(statement)
    print classifier.predict([observe(text)])
else:
    print 'Please submit a valid question / statement.'
