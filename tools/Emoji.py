import re
from .Connection import Connection


class Emoji:
    @staticmethod
    def insert(emoji):
        conn = Connection.get()
        cursor = conn.cursor()

        cursor.execute(
            'INSERT INTO `emojies` (`discord_id`, `name`) VALUES (?, ?)',
            [emoji['id'], emoji['name']]
        )

        conn.commit()

    @staticmethod
    def get_id(emoji):
        conn = Connection.get()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM `emojies` WHERE `discord_id` = ?', [emoji['id']])

        result = cursor.fetchmany(1)

        return 0 if not result else result[0][0]

    @staticmethod
    def get_from_message(message):
        return list(map(
            lambda str: {'id': re.match(r"<:(.+?):(\d+)>", str).group(2), 'name': re.match(r"<:(.+?):(\d+)>", str).group(1)},
            re.findall(r'<:\w{2,}:\d+>', message.content)
        ))
