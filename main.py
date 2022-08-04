import os
import nextcord

client = nextcord.Client(intents=nextcord.Intents(messages=True, message_content=True))
message_count = 0

def reset_count():
  global message_count
  message_count = 0

@client.event
async def on_message(message):
  global message_count
  if message.author.bot:
    return
  if message.content == "?messages":
    await message.reply(f"Count: {message_count}")
    return
  elif message.content == "?update":
    restore_count = message.content.split(" ")[1]
    message_count = int(restore_count)
    await message.reply("Updated")
    return
  message_count += 1

client.run(os.getenv("token"))
