import os

class Config:
    SECRET_KEY = 'your-secret-key-here-change-this'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///time_tracker.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False