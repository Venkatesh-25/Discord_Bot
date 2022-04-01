import discord
import pandas_datareader as web


client = discord.Client()

token = 'xxxxxxxx'

def get_stock_price(ticker):
    data = web.DataReader(ticker, "yahoo")
    return data['Close'].iloc[-1]

@client.event
async def on_connect():
    print("Bot connected to the server!")
    channel = client.get_channel(937761352175476769)
    await channel.send("Just Connected to bot-commands!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send("Hi")

    if message.content == 'Bye':
        await message.author.send("Good bye")

    if message.content.startswith('stockprice'):
        if len(message.content.split(" ")) == 2:
            ticker = message.content.split(" ")[1]
            price = get_stock_price(ticker)
            await message.channel.send(f"Stock price of {ticker} is {price}!")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Welcome to the server {member}")


client.run(token)