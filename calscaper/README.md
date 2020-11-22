# Cal-Scraper
Tools to pull image data and plant information from https://calscape.org/

# Setup
Make sure you have installed all the python requirments in the home directory of this repoistory (Using python 3.7!).

1. In order to prepare the dataset to be used by Google Cloud Vision auto-ml.
    - Run `python download_batch.py`
    - This will step through the websites plant gallery and download them if and only if they have more than 50 images.
    - They will be stored in this directory under images/PLANT_NAME/PLANT_NAME_{SOME_NUMBER}.jpeg
    - If you wish to edit the parameters of the download, simply edit `download_batch.py`
      - `value` and `acceptable_image_count` to modify the intial search and download parameters
<br/>
      
2. We now need to prepare the data to be accepted in Google Vision Auto-ml
    - Before running `generate_csv.py` we need to change `bucket_name` variable inside the python file to configure it for auto-ml
      - e.g. `bucket_name = 'YOUR_BUCKET_NAME_IN_GOOGLE_CLOUD'`
    - This should generate a `.csv` file. This will alow auto-ml to easily find the images and label them for training in your Google Bucket.
      - It should be noted that the generated `image/` folder should not be moved before this step. Otherwise, you will need to edit this file to fix linking issues in auto-ml
<br/>

3. Next step is to upload the images to a Google Cloud Bucket
    - Follow theses [steps](https://cloud.google.com/storage/docs/creating-buckets) in order to create a bucket.
      - At the time of creation of this project, It is important to create the bucket in `us-central-1`. Otherwise, auto-ml will not be able to access the files.
    - After creating the bucket, place the generated `image/` folder in the root directory of your bucket
    - Upload the `.csv` file to the root directory of your bucket
<br/>

4. Go to Google Vision and create a custom model
    - Follow theses [steps](https://cloud.google.com/vision/automl/docs/tutorial) in order to generate a custom model.
<br/>

5. Import the images via `.csv` method in the `IMPORT` tab of Google Vision.
    - After doing all these steps, you are able to train and use your model.
