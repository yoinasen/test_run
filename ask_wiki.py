#!/usr/bin/python

import urllib2
import urllib
import sys

"""
TODO:
move content to a function, have it exception safe.. etc'
"""

def main():
    url = "https://en.wikipedia.org/wiki/"
    keyword = raw_input("what would you like to Wiki search for? ")
    data = {}
    data['search'] = keyword
    data['title'] = 'Search'

    encoded_data = urllib.urlencode(data)
    print encoded_data

    #if neccesary w/o request object full_url = url + '?' + encoded_data
    req = urllib2.Request(url=url, data=encoded_data)
    fp = urllib2.urlopen(req)

    with open("result.html", "wb+") as result_fp:
        result_fp.write(fp.read())
        result_fp.close()



if __name__ == "__main__":
    main()   
