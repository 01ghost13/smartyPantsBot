from tools.database import Database


def change():

    with Database() as db:
        conn = db.connect()
        cursor = conn.cursor()

        cursor.execute("""
                        ALTER TABLE messages
                        ADD COLUMN channel_id TEXT
                        """)
        conn.commit()
        cursor.close()


change()
