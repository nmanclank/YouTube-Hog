# YouTube-Hog



## What is YouTube-Hog-Standalone?
##### A simple Standalone version of a tool to gather random YouTube video data and fill
##### your database. Each video contains multiple fields including:

1. [ ] Channel ID
2. [ ] Channel Title
3. [ ] Video Title
4. [ ] Video ID
5. [ ] Description
6. [ ] Publish date
7. [ ] thumbnail url(s) - Multiple resolutions
8. [ ] Kind - Video type(Short/Video)
9. [ ] etag

##### Along with video information, **some** entries also provide extra data such as:

1. [ ] View Count
2. [ ] Like Count
3. [ ] Favorite Count
4. [ ] Comment(s) Count
5. [ ] Video Tag(s)

# Config:


cfg.py

1. [ ]  `AutoDelete_JSON='True'` If set to false, json files will not be deleted as they're added to db. Only applies to those using a DataBase.

2. [ ] `USE_DATABASE='True'`  If set to false, data will only be stored in json_data dir.


.env

You will NEED to create an env file with the following fields as shown below:

1. [ ] `GOOGLE_CLOUD_API="YOUR API KEY HERE"` 
2. [ ] `RANDOM_ORG_KEY="YOUR API KEY HERE"`
3. [ ] `DatabaseConnection=sqlite:///example.db`

Need more info? Look below under the API Keys Section. I've added links to each respective source.
# Database Setup:
I chose to use SQL Alchemy due to it's flexible approach to database coverage. If you  
have any questions regarding support, you can check out the docs here - https://docs.sqlalchemy.org/en/20/

# To Do:
1. [ ] Config option to have YouTube Hog rest when the query limit has been reached.


# API Keys:

1. [ ] Google Cloud API - https://cloud.google.com/docs/authentication/api-keys
2. [ ] Random.org - https://api.random.org/api-keys

# More? 

For those looking for a **Python library**, I'm already working on a **library version of YouTube Hog**.
I don't yet know when it will be publicly available so please bear with me. Thanks.