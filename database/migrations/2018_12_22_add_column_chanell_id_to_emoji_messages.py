from tools.database import Database


def change():
    conn = Database.connect()
    cursor = conn.cursor()

    cursor.execute("""
                    ALTER TABLE messages
                    ADD COLUMN channel_id TEXT
                    """)
    conn.commit()
    cursor.close()


change()
