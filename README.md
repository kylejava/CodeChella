# @Root4U

## Hackathon Project for #CodeChella hosted by Twitter
### Created by: Ace, Kyle, Neala

## Inspiration
The inspiration for this project was based on seeing Snake plants on different social media platforms and in my own home. Many people owned this and other small plants, but did not know the scientific name or facts about it. Although most plants look similar to each other, they are very different and have a history based on their location. This project was built to help spread awareness and share information on plants, so people can understand where their new decorations came from. Users who also enjoy the outdoors would benefit from this project, as they can send their photo of a plant and receive information about it. We have been indoors for most of the year, so having a project that takes place outdoors would be very refreshing.

## What it does
A user would tweet at @Root4u_ with a picture of a plant and the hashtag #roots. The photo that was tweeted would go through the bot, then go into a machine learning model created in Google Cloud. After the model recognizes the plant in the photo, it will reply back to the user with information regarding the photo such as the scientific name, description, and a link with more information. The model currently only recognizes 39 native Californian trees/plants.

## How we built it
We used Python to utilize the Twitter API to allow us to tweet back to users, notify when the bot is mentioned, and to obtain the picture provided by the user.

We also made use of Google Cloud Platform. We used the storage services to store our training data and Google Vision to create our custom machine learning model.

## Challenges we ran into
Many challenges were faced when working on the project. One challenge faced was trying to figure out how to reply back to a tweet after a user has tweeted to us. Another challenge was getting the media URL because we were having trouble trying to parse through the JSON file. Some of our team members also have limited knowledge in Python, posing another challenge especially with downloading an image using Python.

Another challenge was obtain a dataset for our machine learning model. We didn't know where to find one, so we decided to web scrape a Californian plant/vegetation website in order to obtain our data.

## Accomplishments that we're proud of
One accomplishment we are proud of is the design of the logo and header for the Twitter page. The logo was designed to hopefully create a welcoming page for users to visit.

Another accomplishment we are proud of was being able to connect the Twitter bot to our custom machine learning model in Google Cloud and giving the bot the ability to reply back to the user and recognizing certain words. It was also an accomplishments for some team members to create a project in Python to help expand their knowledge on the language.

We were also pleasantly surprised that our web scraper was able to efficiently grab data from the website. We were worried about how hard parsing the html files on the website would be, however, that was not the case. Each webpage was generated gracefully by the owners of [calscape.org](https://calscape.org/), allowing us to easily grab data from the website.

## What we learned
From this project, we were able to learn how to connect a bot to Google Vision AI and reply back to tweets. We were also able to learn more Python functions and how to web scrape using beautiful soup. We were also able to learn how to use the Twitter API.

## What's next for Root4U
- Expand the dataset in Google Vision AI, we currently only have 39 labels!
- Utilize twitter web hooks to efficiently gather tweet data.
