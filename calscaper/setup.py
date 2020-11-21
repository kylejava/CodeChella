# Informational console screen data.

import calscraper as cs

value = 200
for i in range(value):
	payload = cs.get_payload_for_page(i+1)
	
	imgs = cs.get_images_by_page(payload=payload)
	number_of_imgs = len(imgs)
	
	if number_of_imgs < 50 or number_of_imgs > 100:
		continue

	plant_scientific_name = cs.get_name_for_images(payload=payload)
	if len(plant_scientific_name) == 0:
		continue

	cs.download_images(page_num=i+1, image_urls=imgs, plant_name=plant_scientific_name, payload=payload)