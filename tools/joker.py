import re
import random
import requests
from bs4 import BeautifulSoup


class Joker:
    _source = 'https://bash.im/random'
    _answers = ['ща...'] * 15 + \
               ['ща будет ржака...'] * 15 + \
               ['ожидайте рофла...'] * 15 + \
               ['вкидываю ржомбу...'] * 15 + \
               ['ух, ща бомбезная шутка будет...'] * 5 + \
               ['ща закину анекдот тебе за щеку...'] * 5 + \
               ['засмеялся - с дерьмом в труханах остался))))00'] * 1 + \
               ['я уже читал этот прекол, ебать ржал (нет)...'] * 1 + \
               ['заходят два немца в бар.... а не, это уже была, на эту...'] * 1 + \
               ['в чем разница между твоей мамашей и холодильником? а? а? ну лан, ща...'] * 1
    _request = r'((.*?)бот(.*?)(анекд|шутк|пр[еи]к)(.*?)(хочу|дай|ебани)(.*?))|' \
               r'((.*?)бот(.*?)(хочу|дай|ебани)(.*?)(анекд|шутк|пр[еи]к)(.*?))|' \
               r'((.*?)бот(.*?)хочу\sсмеяться\s(5|пять)\s?мин(.*?))'

    @staticmethod
    async def joke(ctx):
        await ctx.send(random.choice(Joker._answers))

        response = requests.post(url=Joker._source)

        soup = BeautifulSoup(response.text, 'html.parser')
        joke_list = soup.find('div', {'class': 'quote'})

        joke = str(joke_list.find('div', {'class': 'text'})).replace('<br/>', '\n')

        # костыляка
        joke = joke.replace('<div class="text">', '').replace('</div>', '').replace('&lt;', '<').replace('&gt;', '>')

        await ctx.send(f'```{joke}```')

    @staticmethod
    def wants_joke(msg):
        return bool(re.findall(Joker._request, msg, flags=re.IGNORECASE | re.UNICODE))
