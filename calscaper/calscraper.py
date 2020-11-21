import pathlib
import requests
from bs4 import BeautifulSoup

# [Description]
# Returns a list of image urls formatted as a string
# If payload is specified, page_num value is ignored.
#
# [Inputs]
# page_num : INT -> page id of plants
# payLoad : requests object code -> 1xx, 2xx, ..., 5xx
def get_images_by_page(page_num=None, payload=None):
	if payload is None:
		target = 'https://calscape.org/photos/{0}'.format(page_num)
		payload = requests.get(target)

	soup = BeautifulSoup(payload.text, 'lxml')
	divs = soup.find_all(class_='big_image hide')

	image_urls = ['http:' + url.find('img')['src'] for url in divs]
	
	return image_urls

# [Description]
# Gets name of plant by page num
# If payload is specified, page_num value is ignored.
#
# [!!!WARNINGS!!!] 
# Could possibly could return a blank name!
#
# [Inputs]
# page_num : INT -> page id of plant
# payLoad : requests object code -> 1xx, 2xx, ..., 5xx
def get_name_for_images(page_num=None, payload=None):
	if payload is None:
		target = 'https://calscape.org/photos/{0}'.format(page_num)
		payload = requests.get(target)
	
	soup = BeautifulSoup(payload.text, 'lxml')
	header = soup.find('h2')

	return header.contents[0][14:].strip()

# [Description]
# Gets payload of webpage
# Returns a request object
#
# [Remarks]
# This is only created so you do not need to import requests again.
def get_payload_for_page(page_num):
	target = 'https://calscape.org/photos/{0}'.format(page_num)
	payload = requests.get(target)

	return payload

# [Description]
# Downloads an image located at the specified resource location.
#
# [Inputs]
# url : STRING -> specific resource location
# path : STRING -> location to be saved at
def download_image(path, url):
	with requests.get(url, stream=True) as r:
		with open(path, 'wb') as f:
			for chunk in r.iter_content(chunk_size=8192):
				f.write(chunk)

# [Description]
# Downloads images located at the specified resource location.
# Creates a new directory (named after the plant) in the location of the given script.
#
# [Inputs]
# page_num : INT -> page number id
def download_images(page_num, image_urls=None, plant_name=None, payload=None):
	if payload is None:
		target = 'https://calscape.org/photos/{0}'.format(page_num)
		payload = requests.get(target)

	if image_urls is None:
		image_urls = get_images_by_page(payload=payload)
	
	if plant_name is None:
		plant_name = get_name_for_images(payload=payload)

	image_num = 0

	prefix = plant_name.replace(' ', '_').lower()
	pathlib.Path('images/{}/'.format(prefix)).mkdir(parents=True, exist_ok=True)
	path = 'images/{}/{}'.format(prefix, prefix)

	print('Downloading images for {}'.format(plant_name))

	for url in image_urls:
		print(f'... Downloading into {path}_{image_num}.jpeg')
		download_image(f'{path}_{image_num}.jpeg', url)
		image_num = image_num + 1

# [Description]
# Gets the common name of the plant
# Returns a string
#
# [Inputs]
# name : STRING -> scientific name to be searched
def get_description_by_name(name):
	name = name.replace('_', '%20')
	name = name + '(%20)'
	payload = requests.get(f'https://calscape.org/loc-California/{name}')

	soup = BeautifulSoup(payload.text, 'lxml')
	header = soup.find(class_='plant_info')
	return(header.find_all('fieldset')[0].get_text().replace('\n', '').replace('\t', '').strip())