#!/usr/bin/python

import urllib2
import sys

def main():
    url = sys.argv[1]
    fp = urllib2.urlopen(url)
    print fp.read(300)

    print "test"

if __name__ == "__main__":
    main()   
