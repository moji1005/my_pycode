from g4f.client import Client
from balethon import Client

bot = Clinet('539085084:P0PBlUGkLQUUMlj5luSYfbBFsO8Ylgq-1Vw')
@bot.on_message()
async def botgetmesage(piam):
client = Client()
response = client.chat.completions.create(
    model="gpt-4.1",  # Try "gpt-4o", "deepseek-v3", etc.
    messages=[{"role": "user", "content": piam}],
    web_search=False
)
await piam.reply(response.choices[0].message.content)

bot.run()
