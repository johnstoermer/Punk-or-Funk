import numpy as np
import spyscraper as spsc
import csv
from sklearn.utils import shuffle

def getPunk():
    punk = spsc.spyscraper(1)
    punk.findArtists(1,1,'genre:punk')
    punk.findAlbums()
    punk.findTracks()
    return punk.track_analysis_input, punk.track_analysis_output

def getFunk():
    funk = spsc.spyscraper(0)
    funk.findArtists(1,1,'genre:funk')
    funk.findAlbums()
    funk.findTracks()
    return funk.track_analysis_input, funk.track_analysis_output

def main():
    punkin, punkout = getPunk()
    funkin, funkout = getFunk()
    pfunkin = np.array(punkin + funkin)
    pfunkout = np.array(punkout + funkout)
    pfunkin, pfunkout = shuffle(pfunkin, pfunkout, random_state=0) #for some reason i decided to make parallel arrays idk why
    for i in len(pfunkin): #yeah i dont want parallel arrays
        pfunk = pfunkout[i] + pfunkin[i] #yeah im really efficient
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(pfunk)

main()
