import os
import time
import logging
from sqlalchemy import create_engine, Column, Integer, String, Boolean, BigInteger, Text, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker
import cfg
import json


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
dbconnect = cfg.DatabaseConnection

dirc_path = "./json_data/" #Filepath to the dir that included json video data

#sqlalchemy db setup
engine = create_engine(dbconnect, echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()

class Video(Base):
    """Video table class that stores video information."""
    __tablename__ = 'videos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    video_title = Column(String(255))
    channel = Column(String(255))
    video_description = Column(String(255))
    upload_date = Column(String(50))
    yt_view_count = Column(BigInteger)
    yt_tags = Column(Text)
    yt_img_url = Column(String(255))
    yt_like_count = Column(Integer)
    yt_dislike_count = Column(Integer)
    yt_comment_count = Column(Integer)
    favorite_count = Column(Integer)
    video_id = Column(String(11), nullable=False)
    channel_id = Column(String(50))

Base.metadata.create_all(engine)

def add_video_to_db(videos):
    """Function to add videos to the database"""
    videos = videos

    #For each video, check that the vide id doesn't already exist in db
    for video in videos:
        if session.query(Video).filter_by(video_id=video['id']).first():
            logging.info(f"SKIPPING:  {video['id']} already exists")
            continue
        else:

            new_video = Video(

            video_title = video['snippet']['title'],
            channel = video['snippet']['channelTitle'],
            upload_date = video['snippet']['publishedAt'],
            video_id = video['id'],
            channel_id = video['snippet']['channelId']
            )
            if 'description' in video['snippet']: new_video.video_description = video['snippet']['description']
            else: new_video.video_description = "no description"

            if 'viewCount' in video['statistics']: new_video.yt_view_count = video['statistics']['viewCount']
            else: new_video.yt_view_count = "0"

            #Combine tags into a string that's split by our identifier <Splt>
            if 'tags' in video['snippet']:
                tag_string = ""
                tag_splitter = "<Splt>"

                tag_list = video['snippet']['tags']
                for item in tag_list:
                    tag_string += item + tag_splitter

                new_video.yt_tags = tag_string

            else:
                new_video.yt_tags = "none"


            if 'likeCount' in video['statistics']: new_video.yt_like_count = video['statistics']['likeCount']
            else: new_video.yt_like_count = "0"

            if 'commentCount' in video['statistics']: new_video.yt_comment_count = video['statistics']['commentCount']
            else: new_video.yt_comment_count = "0"

            if 'favoriteCount' in video['statistics']: new_video.favorite_count = video['statistics']['favoriteCount']
            else: new_video.favorite_count = "0"

            session.add(new_video)
            session.commit()

            logging.info(f"ID:  {new_video.video_id} - ADDED")


def process_json_data():
    """Function to process video data from json files."""
    try:
        for filename in os.listdir(dirc_path):
            file_path = os.path.join(dirc_path, filename)
            with open(file_path, 'r', encoding="utf-8") as file:
                videos = json.load(file)
                add_video_to_db(videos)
            time.sleep(2)

            if os.path.exists(file_path) and cfg.AutoDelete_JSON == 'True': #If configured to autoDelete JSON, the file will be removed.
                logging.info(f"Files Deleted")
                os.remove(file_path)
            else:
                logging.info("Dir Empty - No Files to Process")
                pass

    except Exception as errr:
        if FileNotFoundError:
            logging.info("No files to process.")
        else:
            logging.error(f"An error occurred: {errr}")

