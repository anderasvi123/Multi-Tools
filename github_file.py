from email.quoprimime import body_check


url = input("Please Url Webhook (Link) : ")
import asyncio
import discord
import time
from discord import Webhook
body_nuke = {
  "content": "Welcome to Multi Tools. Multi Tools are bot and Smart\nYou need one Url Webhook (link) for use",
  "tts": False,
  "embeds": [
    {
      "id": 301618555,
      "title": "Our Discord Server",
      "description": "Discord Multi Tools\n",
      "url": "https://discord.gg/AQVeCT5m",
      "color": 16711680,
      "image": {
        "url": "https://i.postimg.cc/qqy9KhXj/Design-sem-nome-1.png"
      },
      "fields": []
    }
  ],
  "components": [],
  "actions": {},
  "username": "Multi Tools"
}

b1 = "          ███╗   ███╗██╗   ██╗██╗  ████████╗██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗"
b2 = "          ████╗ ████║██║   ██║██║  ╚══██╔══╝██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝"
b3 = "          ██╔████╔██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     ███████╗"
b4 = "          ██║╚██╔╝██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     ╚════██║"
b5 = "          ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║"
b6 = "          ║═╝     ╚═╝ ╚═════╝ ╚═══║══╝╚═╝   ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝"
b7 = "          ║                       ║"
b8 = "          ║═════(1) Send Text     ║═════(4) Change"
b9 = "          ║                       ║"
b10="          ║═════(2) Spam Chat     ║═════(5) Nuke Channel"
b11="          ║                       ║ "
b12="          ║═════(3) Url Webhook   ║═════(6) Exit "
b13="          ║                         "
b14="          ╚═════════════════>"
import aiohttp
async def anything(url):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session=session)
        embed  = discord.Embed(title=text)
        await webhook.send(embed=embed, username=name)
def banner():
    print(b1)
    print(b2)
    print(b3)
    print(b4)
    print(b5)
    print(b6)
    print(b7)
    print(b8)
    print(b9)
    print(b10)
    print(b11)
    print(b12)
    print(b13)
def restart():
    for x in range (3):
        print()
banner()
name = "Smart Bot"
while True:
    main_input = input("          ║═════════════════>")
    if main_input == "1":
        text = input("          ╚Text═════════════>")
        loop =  asyncio.new_event_loop()
        loop.run_until_complete(anything(url))
        loop.close()
        print("-Send-")
        restart()
        banner()
    if main_input == "2":
        spam = input("          ║Count════════════>")
        text = input("          ╚Text═════════════>")
        for i in range(int(spam)):
            loop =  asyncio.new_event_loop()
            loop.run_until_complete(anything(url))
            loop.close()
            print(f"-Send- {i}")
        print("Done")
        restart()
        banner()
    if main_input == "3":
        url = input("          ╚Url══════════════>")
        restart()
        banner()
    if main_input == "4":
        name = input("          ╚Name═════════════>")
        restart()
        banner()
    if main_input == "5":
        yn = input("You Want do it? [Y/N] : ")
        if yn == "N":
            quit()
        spam = input("          ║Count════════════>")
        countdown = input("          ╚Countdown════════>")
        for i in range(int(spam)):
            text = (f"Welcome to Multi Tools. Multi Tools are bot and Smart\nYou need one Url Webhook (link) for use\nhttps://discord.gg/AQVeCT5m")
            name = "Multi Tools"
            loop =  asyncio.new_event_loop()
            loop.run_until_complete(anything(url))
            loop.close()
            time.sleep(float(countdown))
            print(f"-Send- {i}")
        print("-Send- Done")
        restart()
        banner()
    if main_input == "6":
        quit()
banner()