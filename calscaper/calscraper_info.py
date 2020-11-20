# Informational console screen data.

import calscraper as cs

value = 1000
for i in range(value):
	payload = cs.get_payload_for_page(i+1)
	number_of_imgs = len(cs.get_images_by_page(payload=payload))
	if number_of_imgs < 50:
		continue

	plant_scientific_name = cs.get_name_for_images(payload=payload)
	if len(plant_scientific_name) == 0:
		continue

	print('Page {} has {} of plant pictures. The plant\'s scientific name is {}'.format(i, number_of_imgs, plant_scientific_name))