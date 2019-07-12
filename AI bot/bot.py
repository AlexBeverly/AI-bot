#!/usr/bin/env python
#BOT
# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response

#create bot with name "Bot", equivalent responses are chosen randomly, bot will not continue to learn from conversation
bot = ChatBot("Bot",
	response_selection_method = get_random_response,
	read_only = True)

#insert token for Discord bot here
TOKEN = ''
client = discord.Client()

#define response confidence threshold
THRESHOLD = float("0.34")

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if not(message.channel.name == 'bot-chat'):
        return
    if (message.author.bot):
        return

    #get response from input message
    response = bot.get_response(message.content)
    confidence = float(response.confidence)
    #return generic response if confidence is too low
    if (confidence < THRESHOLD):
        response = "I didn't understand that."
    #error caused empty responses, only send response if it exists
    if(len(str(response)) > 1):
        await client.send_message(message.channel, response)
    #print(confidence)
    #print("'",response,"'")
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
