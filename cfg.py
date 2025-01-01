import os
from dotenv import load_dotenv
load_dotenv()

# Main Config file for DataHog
AutoDelete_JSON='True' # If set to false, json files will not be deleted as they're added to db. Only applies to those using DataBase.
USE_DATABASE='True' # If set to false, data will only be stored in json_data dir.


#Database connection - DO NOT CHANGE unless you know what you're doing. Connection info should be placed in .env
DatabaseConnection =os.getenv("DatabaseConnection")

#API KEY Linking - DO NOT CHANGE unless you know what you're doing. API Key should be placed in .env
GOOGLE_CLOUD_API=os.getenv('GOOGLE_CLOUD_API')
RANDOM_ORG_KEY=os.getenv('RANDOM_ORG_KEY')



