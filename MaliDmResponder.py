import discord, os

os.system('pip install discord==1.0.1')
os.system('pip install discord.py==1.6.0')


token = input('Token: ')
replyMessage = input('Message: ')

intents = discord.Intents().all()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
        os.system('clear')
        print(f'          ╔╦╗╔═╗╦  ╦')
        print(f'          ║║║╠═╣║  ║ ')
        print(f'          ╩ ╩╩ ╩╩═╝╩')
        print(f'\n────────────────────────────')
        print(f'\n   Logged in as %s.' % client.user)
        print(f'\n────────────────────────────')
@client.event        
async def on_message(message):
        if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel):
 if message.author.id != client.user.id:
                        await message.reply(replyMessage)
                        print('Replied to %s.' % message.author.name)

if __name__ == '__main__':
    client.run(token, bot=False)
