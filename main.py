import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Estamos logados desde às {0.user} '.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$olá') or message.content.startswith('$ola') or message.content.startswith('$OLA') or message.content.startswith('$OLÁ') or message.content.startswith('$Ola') or message.content.startswith('$Olá') or message.content.startswith('$Oi') or message.content.startswith('$oi'):
    await message.channel.send('Olá, meu nome é {0.user}! Para saber do que eu sou capaz é só digitar $help.'.format(client))
  
  if (message.content.startswith('$help') or message.content.startswith('$Help') or message.content.startswith('$HELP')):
    await message.channel.send('Ai vai alguns comandos que posso fazer: \n - $sci \n - $local \n - $proxima \n')
  
  if (message.content.startswith('$local') or message.content.startswith('$Local') or message.content.startswith('$LOCAL')):
    await message.channel.send('Segue ai o link do Trello da local: \n https://trello.com/b/HUYPAShZ/unico-gest%C3%A3o-local')

  if (message.content.startswith('$proxima') or message.content.startswith('$Proxima') or message.content.startswith('$Próxima') or message.content.startswith('$próxima') or
  message.content.startswith('$PRÓXIMA')):
    await message.channel.send('Segue ai o link do Trello da próxima: \n https://trello.com/b/LPdcldkV/unico-gest%C3%A3o-1211099-18-10-2021')

  if (message.content.startswith('$sci') or message.content.startswith('$SCI') or message.content.startswith('$Sci')):
    await message.channel.send('Com o propósito de FACILITAR A VIDA DO CONTADOR, a SCI Sistemas Contábeis vem apoiando a transformação das empresas contábeis rumo a contabilidade digital, oferecendo tecnologia, inteligência e conhecimento.\n\nNo mercado desde 1991 e 100% brasileira, a SCI Sistemas Contábeis é referência na elaboração de softwares voltados ao segmento contábil... \nQuer saber mais acesse: \n https://www.sci.com.br/empresa/sobre/')

client.run(os.environ['TOKEN'])
