from tools import Database


class Statistic:
    smile_count_sql = """
        select e.name, e.discord_id, count(e_m.id) as smile_count
        from emojies as e
        join emoji_messages as e_m
            on e_m.emoji_id = e.id
        join messages as m
            on m.id = e_m.message_id
        where m.channel_id = '%s'
        group by e.name, e.discord_id
        order by smile_count desc
    """

    @staticmethod
    def smile_count(channel_id):
        with Database() as db:
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute(Statistic.smile_count_sql % channel_id)
            return cursor.fetchall()
