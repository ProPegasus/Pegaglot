from googletrans import Translator
import discord
import emoji
import requests
from langcodes import standardize_tag

translator = Translator()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$'):
#         # await message.channel.send('Hello!')
#         await message.add_reaction('')
#         reacts = message.reactions
#         for i in reacts:
#             print(flag.flag(i.emoji))


@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.author == client.user:
        return
    msg = reaction.message.content
    flag = reaction.emoji
    de_flag = emoji.demojize(flag)
    x = de_flag.replace(':', '')
    if '_' in x:
        x = x.replace('_', ' ')
    if '&' in x:
        x = x.split(' & ')
        x = x[0]
    print(x)

    if x ==  'Iran':
        lan = 'fa'
    elif x == 'Afghanistan':
        lan = 'ps'
    elif x == 'Argentina':
        lan = 'es'
    elif x =='Austria':
        lan = 'de'
    else:
        data = requests.get('https://restcountries.com/v3.1/name/{}'.format(x))
        data = data.json()

        if len(data) > 1:
            lang_list = [*data[1]['languages']]
        else:
            lang_list = [*data[0]['languages']]

        if len(lang_list) > 1 and lang_list[0]=='eng':
            lan = lang_list[1]
        else:
            lan = lang_list[0]

        lan = standardize_tag(lan)

    

    translation = translator.translate(text=msg, dest=lan)
    print(translation.text)
    display_name = reaction.message.author.display_name

    trns_msg = '**' + translation.text + '**' + '\n\n' + 'requested by ' + display_name

    await reaction.message.reply(content=trns_msg)


client.run('MTAxMjQyODgwMjc0OTY0ODk0Ng.GhEaK0.3juQQlpSMWj9qm5cK8aJ5RAhIxVsxb_XvZs7eE')
