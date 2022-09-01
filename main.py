# Make sure to add your discord api token in the last line
from googletrans import Translator
import discord
import emoji
# import requests
# from langcodes import standardize_tag

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
    if ' - ' in x:
        x = x.split(' - ')
        x = x[1]
        
#  *********************************** OLD METHOD ************************************     


#     # googletrans doesn't support some languages so normalising such country's language manually
#     # These are some I found and will be adding more upon testing        
    
#     exp_con = {
#                'Iran': 'fa', 
#                'Afghanistan':'ps', 
#                'Argentina': 'es', 
#                'Austria': 'de', 
#                'Philippines': 'tl'
#               }
#     if exp_con.get(x) != None:
#         lan = exp_con[x]
        
#     else:
#         # Calling the rest countries api with the country name parameter
#         data = requests.get('https://restcountries.com/v3.1/name/{}'.format(x))
#         # converting the data to json
#         data = data.json()
    
    
#         # Some additonal checks to filter out the language code we need from the JSON data
#         if len(data) > 1:
#             lang_list = [*data[1]['languages']]
#         else:
#             lang_list = [*data[0]['languages']]

#         if len(lang_list) > 1 and lang_list[0]=='eng':
#             lan = lang_list[1]
#         else:
#             lan = lang_list[0]
            
            
#         # Converting the 3 letter language code(ISO 639-2) to two letter langauge code (ISO 639-1)
#         lan = standardize_tag(lan)

#  ************************************** NEW METHOD WITH COMPILED DATA TO REMOVE API CALLS **********************************************
    
    data = {"Ascension Island": "en", "Hong Kong": "zh-cn", 'Myanmar': 'my', 'Andorra': 'ca', 'United Arab Emirates': 'ar', 'Afghanistan': 'ps', 'Antigua': 'en', 'Anguilla': 'en', 'Albania': 'sq', 'Armenia': 'hy', 'Angola': 'pt', 'Argentina': 'es', 'American Samoa': 'sm', 'Austria': 'de', 'Australia': 'en', 'Aruba': 'nl', 'Åland Islands': 'sv', 'Azerbaijan': 'az', 'Bosnia': 'bs', 'Barbados': 'en', 'Bangladesh': 'bn', 'Belgium': 'de', 'Burkina Faso': 'fr', 'Bulgaria': 'bg', 'Bahrain': 'ar', 'Burundi': 'fr', 'Benin': 'fr', 'Bermuda': 'en', 'Brunei': 'ms', 'Bolivia': 'es', 'Caribbean Netherlands': 'nl', 'Brazil': 'pt', 'Bahamas': 'en', 'Bhutan': 'hi', 'Bouvet Island': 'no', 'Botswana': 'en', 'Belarus': 'be', 'Belize': 'en', 'Canada': 'fr', 'Cocos (Keeling) Islands': 'en', 'Kinshasa': 'fr', 'Central African Republic': 'fr', 'Brazzaville': 'fr', 'Switzerland': 'fr', 'Cook Islands': 'en', 'Chile': 'es', 'Cameroon': 'fr', 'China': 'zh-cn', 'Colombia': 'es', 'Costa Rica': 'es', 'Cuba': 'es', 'Cape Verde': 'pt', 'Curaçao': 'nl', 'Christmas Island': 'en', 'Cyprus': 'el', 'Czechia': 'cs', 'Germany': 'de', 'Djibouti': 'ar', 'Denmark': 'da', 'Dominica': 'es', 'Dominican Republic': 'es', 'Algeria': 'ar', 'Ecuador': 'es', 'Estonia': 'et', 'Egypt': 'ar', 'Western Sahara': 'ar', 'Eritrea': 'ar', 'Spain': 'es', 'Ethiopia': 'am', 'Finland': 'fi', 'Fiji': 'en', 'Falkland Islands': 'en', 'Micronesia': 'en', 'Faroe Islands': 'da', 'France': 'fr', 'Gabon': 'fr', 'United Kingdom': 'en', 'Grenada': 'en', 'Georgia': 'en', 'French Guiana': 'fr', 'Guernsey': 'fr', 'Ghana': 'en', 'Gibraltar': 'en', 'Greenland': 'en', 'Gambia': 'en', 'Guinea': 'fr', 'Guadeloupe': 'fr', 'Equatorial Guinea': 'fr', 'Greece': 'el', 'South Georgia': 'en', 'Guatemala': 'es', 'Guam': 'en', 'Guinea-Bissau': 'pt', 'Guyana': 'en', 'Heard': 'en', 'Honduras': 'es', 'Croatia': 'hr', 'Haiti': 'fr', 'Hungary': 'hu', 'Indonesia': 'id', 'Ireland': 'en', 'Israel': 'ar', 'Isle of Man': 'en', 'India': 'hi', 'Iraq': 'ar', 'Iran': 'fa', 'Iceland': 'is', 'Italy': 'it', 'Jersey': 'fr', 'Jamaica': 'en', 'Jordan': 'ar', 'Japan': 'ja', 'Kenya': 'sw', 'Kyrgyzstan': 'ky', 'Cambodia': 'km', 'Kiribati': 'en', 'Comoros': 'ar', 'North Korea': 'ko', 'South Korea': 'ko', 'Kuwait': 'ar', 'Cayman Islands': 'en',
            'Kazakhstan': 'kk', 'Laos': 'lo', 'Lebanon': 'ar', 'Liechtenstein': 'de', 'Sri Lanka': 'si',
            'Liberia': 'en', 'Lesotho': 'st', 'Lithuania': 'lt', 'Luxembourg': 'de', 'Latvia': 'lv', 'Libya': 'ar', 'Morocco': 'ar', 'Monaco': 'fr', 'Moldova': 'ro', 'Montenegro': 'en', 'Madagascar': 'fr', 'Marshall Islands': 'en', 'North Macedonia': 'mk', 'Mali': 'fr', 'Mongolia': 'mn', 'Northern Mariana Islands': 'en', 'Martinique': 'fr', 'Mauritania': 'ar', 'Montserrat': 'en', 'Malta': 'mt', 'Mauritius': 'fr', 'Maldives': 'en', 'Malawi': 'ny', 'Mexico': 'es', 'Malaysia': 'ms', 'Mozambique': 'pt', 'Namibia': 'af', 'New Caledonia': 'fr', 'Niger': 'fr', 'Norfolk Island': 'en', 'Nigeria': 'en', 'Nicaragua': 'es', 'Netherlands': 'nl', 'Norway': 'no', 'Nepal': 'ne', 'Nauru': 'en', 'Niue': 'en', 'New Zealand': 'mi', 'Oman': 'ro', 'Panama': 'es', 'Peru': 'es', 'French Polynesia': 'fr', 'Papua New Guinea': 'en', 'Philippines': 'tl', 'Pakistan': 'ur', 'Poland': 'pl', 'Pitcairn Islands': 'en', 'Puerto Rico': 'es', 'Portugal': 'pt', 'Palau': 'en', 'Paraguay': 'es', 'Qatar': 'ar', 'Réunion': 'fr', 'Romania': 'ro', 'Serbia': 'sr', 'Russia': 'ru', 'Rwanda': 'fr', 'Saudi Arabia': 'ar', 'Solomon Islands': 'en', 'Seychelles': 'fr', 'Sudan': 'en', 'Sweden': 'sv', 'Singapore': 'ms', 'St. Helena': 'en', 'Slovenia': 'sl', 'Svalbard': 'no', 'Slovakia': 'sk', 'Sierra Leone': 'en', 'San Marino': 'it', 'Senegal': 'fr', 'Somalia': 'ar', 'Suriname': 'nl', 'South Sudan': 'en', 'São Tomé': 'pt', 'El Salvador': 'es', 'Sint Maarten': 'fr', 'Syria': 'ar', 'Eswatini': 'en', 'Tristan da Cunha': 'en', 'Turks': 'en', 'Chad': 'ar', 'French Southern Territories': 'fr', 'Togo': 'fr', 'Thailand': 'th', 'Tajikistan': 'ru', 'Tokelau': 'sm', 'Timor-Leste': 'pt', 'Turkmenistan': 'ru', 'Tunisia': 'ar', 'Tonga': 'en', 'Turkey': 'tr', 'Trinidad': 'en', 'Tuvalu': 'en', 'Taiwan': 'zh-tw', 'Tanzania': 'sw', 'Ukraine': 'uk', 'Uganda': 'sw', 'United States': 'en', 'Uruguay': 'es', 'Uzbekistan': 'ru', 'Vatican City': 'it', 'Venezuela': 'es', 'Vietnam': 'vi', 'Vanuatu': 'es', 'Wallis': 'fr', 'Samoa': 'sm', 'Kosovo': 'sq', 'Yemen': 'ar', 'Mayotte': 'fr', 'South Africa': 'af', 'Zambia': 'en', 'Zimbabwe': 'sn'}

    if data.get(x) != None:
        lan = data[x]
    else:
        lan = "en"
    
    # Translating using googletrans translator
    translation = translator.translate(text=msg, dest=lan)
    # Getting the username of the one that added the reaction
    display_name = user.display_name
    # Styling the message and adding the name of the user that requested the translation at the end of message
    trns_msg = '**' + translation.text + '**' + '\n\n' + 'requested by ' + display_name
    # Sending the message
    await reaction.message.reply(content=trns_msg)


client.run('YOUR DISCORD TOKEN') # <---- Your discord api token here
