from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
import time
import spotipy

client_credentials_manager = SpotifyClientCredentials(GET YA OWN CREDENTIALS)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

class spyscraper:
    def __init__(self,output_id):
        self.artist_ids = []
        self.artist_names = []
        self.album_ids = []
        self.album_names = []
        self.track_ids = []
        self.track_names = []
        self.track_analysis = []
        self.output_id = output_id
    
    def findArtists(self, lim, maxPage, q_value):
        for i in range(maxPage):
            results = sp.search(q=q_value,type='artist',limit=lim,offset=i*lim)
            artists = results['artists']['items']
            print('Finding Artists on page '+str(i+1)+':', end=' ')
            for j in range(len(artists)):
                self.artist_ids.append(artists[j]['id'])
                self.artist_names.append(artists[j]['name'])
                #print('Got',artists[j]['name'])
                #print('I\'m '+str(int(((j+1)/len(artists))*100))+'% done with finding artists')
                if int(((j+2)/len(artists))*10) > int(((j+1)/len(artists))*10):
                    print('|', end='')
            print('\n')

    def findAlbums(self):
        print('Finding Albums:', end=' ')
        for i in range(len(self.artist_ids)):
            results = sp.artist_albums(self.artist_ids[i],album_type='album')
            albums = results['items']
            for j in range(len(albums)):
                if albums[j]['name'] not in self.album_names:
                    self.album_ids.append(albums[j]['id'])
                    self.album_names.append(albums[j]['name'])
                    print('Got',albums[j]['name'])
                    #print('I\'m '+str(int(((j+1)/len(albums))*100))+'% done with '+str(self.artist_names[i]))
            if int(((i+2)/len(self.album_ids))*10) > int(((i+1)/len(self.album_ids))*10):
                    print('|', end='')
        print('\n')

    def findTracks(self):
        print('Finding Tracks:', end=' ')
        for i in range(len(self.album_ids)):
            results = sp.album(self.album_ids[i])
            tracks = results['tracks']['items']
            current_tracks = []
            for j in range(len(tracks)):
                if tracks[j]['name'] not in self.track_names:
                    current_tracks.append(tracks[j]['id'])
                    #self.track_ids.append(tracks[j]['id'])
                    self.track_names.append(tracks[j]['name'])
                    #print('Got',tracks[j]['name'])
                    #print('I\'m '+str(int(((j+1)/len(tracks))*100))+'% done with '+str(self.album_names[i]))
            self.findTrackAnalysis(current_tracks)
            if int(((i+2)/len(self.album_ids))*10) > int(((i+1)/len(self.album_ids))*10):
                    print('|', end='')
        print('\n')

    def findTrackAnalysis(self,track_ids):
        results = sp.audio_features(track_ids)
        for i in range(len(results)):
            try:
                single_track_analysis = [results[i]['energy'],results[i]['liveness'],results[i]['valence'],results[i]['time_signature'],
                                  results[i]['danceability'],results[i]['instrumentalness'],results[i]['tempo'],results[i]['loudness'],
                                  results[i]['mode'],results[i]['key'],results[i]['acousticness'],results[i]['speechiness']]
                self.track_analysis.append([self.output_id] + single_track_analysis)
            except TypeError:
                '''
                print('Oops!')
            print('Finding Analysis: '+str(int(((i+1)/len(results))*100))+'%')
            '''
