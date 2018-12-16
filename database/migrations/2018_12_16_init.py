import sqlite3


conn = sqlite3.connect('../database.sqlite')
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE `emojies` (
    `id`          INTEGER PRIMARY KEY AUTOINCREMENT,
    `discord_id`  TEXT,
    `name`        TEXT
)
""")

cursor.execute("""
CREATE TABLE `messages` (
    `id`          INTEGER PRIMARY KEY AUTOINCREMENT,
    `discord_id`  TEXT,
    `author`      TEXT,
    `channel`     TEXT,
    `content`     TEXT,
    `created_at`  TEXT
)
""")

cursor.execute("""
CREATE TABLE `emoji_messages` (
    `id`          INTEGER PRIMARY KEY AUTOINCREMENT,
    `message_id`  INTEGER,
    `emoji_id`    TEXT,
    `emoji_name`  TEXT
)
""")

cursor.execute("""
CREATE UNIQUE INDEX IF NOT EXISTS discord_id_unique ON emojies (discord_id)
""")

conn.commit()
