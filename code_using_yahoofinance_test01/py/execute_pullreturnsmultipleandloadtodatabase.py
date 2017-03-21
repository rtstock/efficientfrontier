#!/usr/bin/env python

import os, sys, time

def files_to_timestamp(path):
    files = [os.path.join(path, f) for f in os.listdir(path)]
    return dict ([(f, os.path.getmtime(f)) for f in files])

if __name__ == "__main__":
    print '-----------------------'
    print 'First arg',sys.argv[0]
    print 'Second arg',sys.argv[1]
    print 'Third arg',sys.argv[2]
    print 'Fourth arg',sys.argv[3]
    print 'Fifth arg',sys.argv[4]
    import pullreturnsmultipleandloadtodatabase
    o = pullreturnsmultipleandloadtodatabase.perform(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
