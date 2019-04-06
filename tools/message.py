from .Emoji import Emoji
from .database import Database


class Message:
    @staticmethod
    def insert(message):
        with Database() as db:
            conn = db.connect()
            cursor = conn.cursor()

            cursor.execute(
                'INSERT INTO messages '
                '(discord_id, author, channel, channel_id, content, created_at) '
                'VALUES (%s, %s, %s, %s, %s, %s) RETURNING id',
                (
                    message.id,
                    message.author.id,
                    message.channel.name,
                    message.channel.id,
                    message.content,
                    message.created_at.strftime('%Y-%m-%d %H:%M:%S')
                )
            )

            conn.commit()
            inserted_id = cursor.fetchone()
            cursor.close()

            return inserted_id

    @staticmethod
    def insert_emojies(message_id, emojies):
        with Database() as db:
            conn = db.connect()
            cursor = conn.cursor()

            for emoji in emojies:
                id = Emoji.get_id(emoji)

                if not id:
                    Emoji.insert(emoji)
                    id = Emoji.get_id(emoji)

                cursor.execute(
                    'INSERT INTO emoji_messages (message_id, emoji_id) VALUES (%s, %s)',
                    (message_id, id)
                )

            conn.commit()
            cursor.close()
