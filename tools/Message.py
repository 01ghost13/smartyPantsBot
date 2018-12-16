from .Emoji import Emoji
from .Connection import Connection


class Message:
    @staticmethod
    def insert(message):
        conn = Connection.get()
        cursor = conn.cursor()

        cursor.execute(
            'INSERT INTO `messages` (`discord_id`, `author`, `channel`, `content`, `created_at`) VALUES (?, ?, ?, ?, ?)',
            [
                message.id,
                message.author.id,
                message.channel.name,
                message.content,
                message.created_at.strftime('%Y-%m-%d %H:%M:%S')
            ]
        )

        conn.commit()

        return cursor.lastrowid

    @staticmethod
    def insert_emojies(message_id, emojies):
        conn = Connection.get()
        cursor = conn.cursor()

        for emoji in emojies:
            id = Emoji.get_id(emoji)

            if not id:
                Emoji.insert(emoji)
                id = Emoji.get_id(emoji)

            cursor.execute(
                'INSERT INTO `emoji_messages` (`message_id`, `emoji_id`) VALUES (?, ?)',
                [message_id, id]
            )

        conn.commit()
