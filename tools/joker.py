import re
import random
import requests
from bs4 import BeautifulSoup


class Joker:
    _source = 'https://bash.im/random'
    _answers = ['ща...'] * 10 + \
               ['ща будет ржака...'] * 10 + \
               ['ожидайте рофла...'] * 10 + \
               ['вкидываю ржомбу...'] * 10 + \
               ['сбрасываю ржомбу...'] * 10 + \
               ['ух, ща бомбезная шутка будет...'] * 10 + \
               ['ща закину анекдот тебе за щеку...'] * 10 + \
               ['засмеялся - с дерьмом в труханах остался))))00'] * 5 + \
               ['я уже читал этот прекол, ебать ржал (нет)...'] * 5 + \
               ['заходят два немца в бар.... а не, это уже была, на эту...'] * 5 + \
               ['в чем разница между твоей мамашей и холодильником? а? а? ну лан, ща...'] * 5
    _request = r'((.*?)бот(.*?)(анекд|шутк|пр[еи]к)(.*?)(хочу|дай|ебани)(.*?))|' \
               r'((.*?)бот(.*?)(хочу|дай|ебани)(.*?)(анекд|шутк|пр[еи]к)(.*?))|' \
               r'((.*?)бот(.*?)хочу\sсмеяться\s(5|пять)\s?мин(.*?))'

    @staticmethod
    async def joke(ctx):
        await ctx.send(random.choice(Joker._answers))

        response = requests.post(url=Joker._source)

        soup = BeautifulSoup(response.text, 'html.parser')
        joke_list = soup.find('article', {'class': 'quote'})

        joke = str(joke_list.find('div', {'class': 'quote__body'})).replace('<br/>', '\n')

        # костыляка
        joke = joke.replace('<div class="quote__body">', '').replace('</div>', '').replace('&lt;', '<').replace('&gt;', '>')

        await ctx.send(f'```{joke}```')

    @staticmethod
    def wants_joke(msg):
        return bool(re.findall(Joker._request, msg, flags=re.IGNORECASE | re.UNICODE))
