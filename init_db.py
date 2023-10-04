"""
initiate the database
"""

import sqlite3
from model import User, Survey, Question, QuestionAnswer, QuestionType, SurveyState
from app import db

with sqlite3.connect("survey.db") as connection:
    # create all the tables
    c = connection.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        name TEXT NOT NULL,
        password TEXT NOT NULL,
        profile_image TEXT NOT NULL DEFAULT "user_icon.png"
        )"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS survey(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        state INTEGER NOT NULL,
        time_created DATETIME NOT NULL,
        rating FLOAT DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
        )"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS question(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            survey_id INTEGER NOT NULL,
            position INTEGER NOT NULL,
            type INTEGER NOT NULL,
            title TEXT NOT NULL,
            FOREIGN KEY (survey_id) REFERENCES survey(id) ON DELETE CASCADE
            )"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS question_answer(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            answer_number INTEGER,
            timestamp DATETIME NOT NULL,
            selected INTEGER,
            text TEXT,
            number INTEGER,
            question_id INTEGER NOT NULL,
            FOREIGN KEY (question_id) REFERENCES question(id) ON DELETE CASCADE
            )"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS choice(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER NOT NULL,
            text TEXT NOT NULL,
            number INTEGER,
        FOREIGN KEY (question_id) REFERENCES question(id) ON DELETE CASCADE
        )"""
    )

    # create a default user
    c.execute(
        """INSERT OR IGNORE INTO user(email, name, password)
        VALUES('user@email.es', 'User', '')
        """
    )

    # commit changes
    connection.commit()

    
