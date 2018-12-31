from tools.database import Database


def change():

    with Database() as db:
        conn = db.connect()
        cursor = conn.cursor()

        cursor.execute("""
                        ALTER TABLE emoji_messages 
                        ALTER COLUMN emoji_id TYPE INTEGER using emoji_id::integer
                        """)
        cursor.execute("""
                        ALTER TABLE messages 
                        ALTER COLUMN created_at TYPE TIMESTAMP using created_at::timestamp
                        """)
        conn.commit()
        cursor.close()


change()
