# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 17:05:40 2017

@author: Christopher
"""

import json
import requests
#import sys
#
#temp = sys.stdout
#sys.stdout = open("artist_info.txt", "w")
BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

# query parameters are given to the requests.get function as a dictionary; this
# variable contains some starter parameters.
query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    # This is the main function for making queries to the musicbrainz API.
    # A json document should be returned by the query.
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    # This adds an artist name to the query parameters before making
    # an API call to the function above.
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    # After we get our output, we can format it to be more readable
    # by using this function.
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():
    '''
    Modify the function calls and indexing below to answer the questions on
    the next quiz. HINT: Note how the output we get from the site is a
    multi-level JSON document, so try making print statements to step through
    the structure one level at a time or copy the output to a separate output
    file.
    '''
    results = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
    pretty_print(results["artists"])

    print "\nLIFE SPANS:"
    for artist in results["artists"]:
        if "life-span" in artist:
            print artist["life-span"]

#    artist_id = results["artists"][1]["id"]
#    print "\nARTIST:"
#    pretty_print(results["artists"][1])
#
#    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
#    releases = artist_data["releases"]
#    
#    print "\nONE RELEASE:"
#    pretty_print(releases[0], indent=2)
#    release_titles = [r["title"] for r in releases]
#        
#    
#    print "\nALL TITLES:"
#    for t in release_titles:
#        print t


if __name__ == '__main__':
    main()
#    sys.stdout.close()
#    sys.stdout = temp
