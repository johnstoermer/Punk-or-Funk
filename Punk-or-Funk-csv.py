import numpy as np
import spyscraper as spsc
import csv
import random

csvfile = "data.csv"

def getPunk():
    punk = spsc.spyscraper(1)
    punk.findArtists(1,1,'genre:punk')
    punk.findAlbums()
    punk.findTracks()
    return punk.track_analysis

def getFunk():
    funk = spsc.spyscraper(0)
    funk.findArtists(1,1,'genre:funk')
    funk.findAlbums()
    funk.findTracks()
    return funk.track_analysis

def main():
    pfunk = getPunk() + getFunk()
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(pfunk)

main()
