# Downloads a batch of images

import calscraper as cs

# Determines how far we step through the gallery to download images
value = 1000
# This parameter determines if the plant gallery is sufficient enough to download.
# If the gallery has less than acceptable_image_count_low, the gallery will not be downloaded.
# If the gallery has more than acceptable_image_count_high, the gallery will not be downloaded.
acceptable_image_count_low = 50
acceptable_image_count_high = 50

for i in range(value):
	payload = cs.get_payload_for_page(i+1)
	
	imgs = cs.get_images_by_page(payload=payload)
	number_of_imgs = len(imgs)
	
	if number_of_imgs < acceptable_image_count_low or number_of_imgs > acceptable_image_count_high:
		continue

	plant_scientific_name = cs.get_name_for_images(payload=payload)
	if len(plant_scientific_name) == 0:
		continue

	cs.download_images(page_num=i+1, image_urls=imgs, plant_name=plant_scientific_name, payload=payload)