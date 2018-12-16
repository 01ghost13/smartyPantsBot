import re
from .database import Database


class Emoji:
    @staticmethod
    def insert(emoji):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            'INSERT INTO emojies (discord_id, name) VALUES (%s, %s)',
            (emoji['id'], emoji['name'])
        )

        conn.commit()
        cursor.close()

    @staticmethod
    def get_id(emoji):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM emojies WHERE discord_id = %s', (emoji['id'],))

        result = cursor.fetchmany(1)

        return 0 if not result else result[0][0]

    @staticmethod
    def get_from_message(message):
        return list(map(
            lambda str: {'id': re.match(r"<:(.+?):(\d+)>", str).group(2), 'name': re.match(r"<:(.+?):(\d+)>", str).group(1)},
            re.findall(r'<:\w{2,}:\d+>', message.content)
        ))
