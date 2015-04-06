#!/bin/usr/env python
import urllib
import json
import os
import webbrowser

""" This function captures the user input mainly the movie name """


def Call_Api(movie_name):
	print "Your Movie details are being Exracted. Please hold on for a momnet"
	print "Fetching Data....."
	request=urllib.urlopen("http://www.omdbapi.com/?t="+movie_name)
	movie_details=request.read()
	request.close()
	movie_json=json.loads(movie_details)
	response=movie_json.get('Response')
	if response=='False':
		print "You have misspelled the Name or the Movie you are searching for is not available in our Database"
	else:
		print movie_json		
		plot=movie_json.get("Plot")
		language=movie_json.get("Language")
		rating=movie_json.get("imdbRating")
		director=movie_json.get("Director")
		actors=movie_json.get("Actors")
		genre=movie_json.get("Genre")
		runtime=movie_json.get("Runtime")
		imdbid=movie_json.get("imdbID")
		print "------------------------------------"
		print "Plot:",plot
		print "Language:",language
		print "IMDB Rating:", rating
		print "Director:",director
		print "Actors:",actors
		print "Genre:",genre
		print "Runtime:",runtime
		print "-------------------------------------"
		print "Do you wish to open the details on IMBD website on your browser?"
		print "y/n?"
		wish=raw_input()
		if wish=='y' or wish=='Y':
			webbrowser.open("http://www.imdb.com/title/"+imdbid)
def input():
	print "Enter the Movie"
	name=raw_input()
	if name:
		Call_Api(name)
	else:
		print "oops!! You seem to have not entered any data" 	
		

input()

 
