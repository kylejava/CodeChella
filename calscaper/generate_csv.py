import glob
import pathlib

bucket_name='cali_veg_v1'

img_loc=pathlib.Path('images/')
folders=[x for x in img_loc.iterdir() if x.is_dir()]

#images= [pathlib.Path(img).name for folder in folders for img in list(pathlib.Path(folder).glob('*.jpeg'))]

pathlib.Path(folders[0]).name
#print(images)

with open('labels.csv', 'w') as file:
	for folder in folders:
		path=pathlib.Path(folder)
		label=path.name
		images=[pathlib.Path(f_name).name for f_name in list(folder.glob('*.jpeg'))]
		
		for img in images:
			file.write(f'gs://{bucket_name}/images/{label}/{img},{label}\n')
