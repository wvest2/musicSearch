from flask import Flask, request
from app import wikipedia, spotify, artistTweets

@app.route("/")
def index():
	return "This engine allows you to query an artist/song for a wikipedia exerpt, spotify playlist, and tweets about the artist"
	pass

@app.route("/artist/<input>")
def artistSearch(input):
	wikipedia(input)
	spotifyArtist(input)
	artistTweets(input)
	pass

@app.route("/song/<input>")
def songSearch(input):	
	wikipedia(input)
	spotifySong(input)
	artistTweets(input)
	pass