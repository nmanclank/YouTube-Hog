import os
import logging
from sqlalchemy import create_engine, Column, Integer, String, Boolean, BigInteger, Text, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker
import cfg

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
dbconnect = cfg.DatabaseConnection

dirc_path = "./json_data/json_data" #Filepath to the dir that included json video data

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