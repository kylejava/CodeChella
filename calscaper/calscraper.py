import requests
from bs4 import BeautifulSoup

# Returns a list of urls formatted as a string
# page_num : INT -> page id of plants
def get_images_by_page(page_num):
	target = 'https://calscape.org/photos/{0}'.format(page_num)
	payload = requests.get(target)

	soup = BeautifulSoup(payload.text, 'lxml')
	divs = soup.find_all(class_='big_image hide')

	image_urls = ['http:' + url.find('img')['src'] for url in divs]
	
	return image_urls

# Downloads an image located at the specified resource location.
# url : STRING -> specific resource location
# path : STRING -> 
def download_image(url, path):
	with requests.get(url, stream=True) as r:
		with open(path, 'wb') as f:
			for chunk in r.iter_content(chunk_size=8192):
				f.write(chunk)
