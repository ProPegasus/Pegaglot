# Make sure to add your discord api token in the last line
from googletrans import Translator
import discord
import emoji
import requests
from langcodes import standardize_tag

# Initialising the translator
translator = Translator()


# Specifying the bot intents
# (You will need to enable the required intent toggles in your discord developer dashboard)
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Initialisation of the bot
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# The function that comes into play when it detects a reaction to a message
@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.author == client.user:
        return
    
    # Get the message content
    msg = reaction.message.content
    
    
    # Get the reaction emoji 
    # note: It recieves all the emojis and throws an error if it's not a flag which the discord api will ignore
    flag = reaction.emoji
    
    
    # Convet the emoji to text
    de_flag = emoji.demojize(flag)
    
    
    # Filters to get perfect name of the country
    x = de_flag.replace(':', '')
    if '&' in x:
        x = x.split(' & ')
        x = x[0]
    if '_' in x:
        x = x.replace('_', ' ')
        
        
    # googletrans doesn't support some languages so normalising such country's language manually
    # These are some I found and will be adding more upon testing        
    
    exp_con = {
               'Iran': 'fa', 
               'Afghanistan':'ps', 
               'Argentina': 'es', 
               'Austria': 'de', 
               'Philippines': 'tl'
              }
    if exp_con.get(x) != None:
        lan = exp_con[x]
        
    else:
        # Calling the rest countries api with the country name parameter
        data = requests.get('https://restcountries.com/v3.1/name/{}'.format(x))
        # converting the data to json
        data = data.json()
    
    
        # Some additonal checks to filter out the language code we need from the JSON data
        if len(data) > 1:
            lang_list = [*data[1]['languages']]
        else:
            lang_list = [*data[0]['languages']]

        if len(lang_list) > 1 and lang_list[0]=='eng':
            lan = lang_list[1]
        else:
            lan = lang_list[0]
            
            
        # Converting the 3 letter language code(ISO 639-2) to two letter langauge code (ISO 639-1)
        lan = standardize_tag(lan)

    
    # Translating using googletrans translator
    translation = translator.translate(text=msg, dest=lan)
    # Getting the username of the one that added the reaction
    display_name = user.display_name
    # Styling the message and adding the name of the user that requested the translation at the end of message
    trns_msg = '**' + translation.text + '**' + '\n\n' + 'requested by ' + display_name
    # Sending the message
    await reaction.message.reply(content=trns_msg)


client.run('YOUR DISCORD TOKEN') # <---- Your discord api token here
