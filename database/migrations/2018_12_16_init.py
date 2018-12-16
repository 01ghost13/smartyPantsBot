from tools.database import Database


def change():
    conn = Database.connect()
    cursor = conn.cursor()

    cursor.execute("""
                    CREATE TABLE emojies (
                        id          BIGSERIAL PRIMARY KEY,
                        discord_id  TEXT,
                        name        TEXT
                    )
                    """)

    cursor.execute("""
                    CREATE TABLE messages (
                        id          BIGSERIAL PRIMARY KEY,
                        discord_id  TEXT,
                        author      TEXT,
                        channel     TEXT,
                        content     TEXT,
                        created_at  TEXT
                    )
                    """)

    cursor.execute("""
                    CREATE TABLE emoji_messages (
                        id          BIGSERIAL PRIMARY KEY,
                        message_id  INTEGER,
                        emoji_id    TEXT
                    )
                    """)

    cursor.execute("""
                CREATE UNIQUE INDEX IF NOT EXISTS discord_id_unique ON emojies (discord_id)
                """)

    conn.commit()
    cursor.close()


change()
