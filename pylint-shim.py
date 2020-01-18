#!/usr/bin/env python
import sys
import subprocess as subp
import re
import argparse

SUMMARY_LINE=re.compile('Your code has been rated at ([0-9.]+)/10')

def run_pylint():
    """run pylint with a pre-commit wrapper"""

    parser = argparse.ArgumentParser()
    parser.add_argument('--error-threshold', type=float, default=9.9999999999)
    score_opts, remaining_args = parser.parse_known_args( sys.argv[1:] )
    threshold_score=vars(score_opts)['error_threshold'] 
    msg="PyLint Required Minimum Score: {0}".format(threshold_score)
    print(msg)
   
    cmd = ["pylint"] + remaining_args
    results = subp.run( cmd, stdout=subp.PIPE)
    
    data = results.stdout.decode('utf-8')
    print(data)
    
    # Check the output...
    score=SUMMARY_LINE.search(data)
    if not score:
        print('Unable to find the summary line!')
        exit(1)
    
    numeric_score = float(score.groups()[0])
    if numeric_score >= threshold_score:
       print('*'*80)
       print("PyLint Score satisfies minimum score: {0}".format(threshold_score))
       print('*'*80)
       exit(0)
    
    print('*'*80)
    print("PYLINT SCORE DID NOT SATISFY MINIMUM SCORE: ".format(threshold_score))
    print('*'*80)
    exit(1)


run_pylint()

