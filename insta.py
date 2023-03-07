import requests
def insta(link):
	url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

	querystring = {"url":link}

	headers = {
		"X-RapidAPI-Key": "64b5f788b5mshd9452863cc50d31p1a9174jsna667ab7e79c4",
		"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring).json()
	return {'video': response['media']}
