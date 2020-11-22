# Informational console screen data.

import calscraper as cs

# Determines how far we step through the gallery to download images
value = 1000
# This parameter determines if the plant gallery is sufficient enough to download.
# If the gallery has less than acceptable_image_count, the gallery will not be downloaded.
acceptable_image_count = 50

for i in range(value):
	payload = cs.get_payload_for_page(i+1)
	number_of_imgs = len(cs.get_images_by_page(payload=payload))
	if number_of_imgs < acceptable_image_count:
		continue

	plant_scientific_name = cs.get_name_for_images(payload=payload)
	if len(plant_scientific_name) == 0:
		continue

	print('Page {} has {} of plant pictures. The plant\'s scientific name is {}'.format(i, number_of_imgs, plant_scientific_name))