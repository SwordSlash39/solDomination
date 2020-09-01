import discord
import time
import random
import math
client = discord.Client()
token = '---'
players_playing = []
passive = []
guilds = []
# Coins, coal, soldiers, rbs, cost (in Gems)
offers = []
dungeons = []

# Prefix and admnis
default_call = 'sol '
authorised = []     # Add you name and tag here, if you want to be an authorised player

# Other vars
cost = 0
keyword = ''
event_on = False
words = ['grab', 'snatch', 'steal', 'take', 'hold']
chan = ''
updating = False
channel_event = ''
banned = []
msg = ''


def findPlayer(player):
    for i in range(len(players_playing)):
        if str(players_playing[i][0]) == str(player):
            return i
    return "nil"


def lpassiveFind(player):
    for i in range(len(passive)):
        if str(passive[i][0]) == str(player):
            return i
    return "nil"


def dungeonFind(player):
    for i in range(len(dungeons)):
        if str(player) in dungeons[i]:
            return i
    return "nil"


def guildFind(player):
    for i in range(len(guilds)):
        if str(guilds[i][0][0]) == str(player):
            return i
    return "nil"


def inGuild(player):
    for i in range(len(guilds)):
        if str(player) in guilds[i]:
            return True
    return False


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="solDomination"))


@client.event
async def on_message(message):
    global output, keyword, event_on, words, cost, phiminfo, pinfo, passive, updating, channel_event, offline, offers, guilds, entity, dungeons, banned, msg
    if message.author == client.user:
        return
    if message.author.bot:
        return
    if not updating or str(message.author) in authorised:
        if message.content.lower() == str(default_call) + 'start':
            if findPlayer(str(message.author)) == 'nil':
                if str(message.author) not in banned:
                    # name, time, banklvl, soldierlvl, soldieramt, money, insta-cash, [coal, nukes], currentMultiplier, rb's, [books], sharpMultiplier, lootingMultiplier
                    players_playing.append([str(message.author), round(time.time()), 1, 1, 0, 0, 0, [0, 0], 1, 0, [], 1, 1, 0, ''])
                    msg = discord.Embed(title="Hello!",
                                        description="Thanks for creating your account, " + str(message.author.mention) + "! Enjoy playing solDomination :)",
                                        color=discord.Color.green())
                    msg.set_author(name="solDomination")
                    msg.set_thumbnail(
                        url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                    await message.channel.send(embed=msg)
                else:
                    msg = discord.Embed(title="Error",
                                        description="You have been banned from solDomination",
                                        color=discord.Color.red())
                    msg.set_author(name="solDomination")
                    msg.set_thumbnail(
                        url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                    await message.channel.send(embed=msg)
            else:
                msg = discord.Embed(title="Error",
                                        description="You already have an account!",
                                        color=discord.Color.red())
                msg.set_author(name="solDomination")
                msg.set_thumbnail(url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                await message.channel.send(embed=msg)

        if message.content.lower() == str(default_call) + 'upgrade bank' or message.content.lower() == str(default_call) + 'up b':
            if findPlayer(str(message.author)) != 'nil':
                print(findPlayer(str(message.author)))
                if players_playing[findPlayer(str(message.author))][5] >= players_playing[findPlayer(str(message.author))][2] * 1000:
                    players_playing[findPlayer(str(message.author))][5] -= int(players_playing[findPlayer(str(message.author))][2] * 1000)
                    players_playing[findPlayer(str(message.author))][2] += 1
                    msg = discord.Embed(title="Success!",
                                        description=str(message.author.mention) + ", you upgraded your bank level by 1!",
                                        color=discord.Color.green())
                    msg.set_author(name="solDomination")
                    msg.set_thumbnail(
                        url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                    await message.channel.send(embed=msg)
                else:
                    msg = discord.Embed(title="Error",
                                        description=str(message.author.mention) + ", you do not enough money! You need $" + str(players_playing[findPlayer(str(message.author))][2] * 1000) + " to upgrade your bank!",
                                        color=discord.Color.red())
                    msg.set_author(name="solDomination")
                    msg.set_thumbnail(
                        url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                    await message.channel.send(embed=msg)

            else:
                msg = discord.Embed(title="Error",
                                    description="Create an account first!",
                                    color=discord.Color.red())
                msg.set_author(name="solDomination")
                msg.set_thumbnail(url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                await message.channel.send(embed=msg)

        if message.content.lower() == str(default_call) + 'upgrade soldier' or message.content.lower() == str(default_call) + 'up s':
            if findPlayer(str(message.author)) != 'nil':
                if players_playing[findPlayer(str(message.author))][5] >= players_playing[findPlayer(str(message.author))][3] * 2000:
                    players_playing[findPlayer(str(message.author))][5] -= int(players_playing[findPlayer(str(message.author))][3] * 2000)
                    players_playing[findPlayer(str(message.author))][3] += 1
                    msg = discord.Embed(title="Success!",
                                        description=str(
                                            message.author.mention) + ", you upgraded your soldier level by 1!",
                                        color=discord.Color.green())
                    msg.set_author(name="solDomination")
                    msg.set_thumbnail(
                        url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                    await message.channel.send(embed=msg)
                else:
                    msg = discord.Embed(title="Error",
                                        description=str(
                                            message.author.mention) + ", you do not enough money! You need $" + str(players_playing[findPlayer(str(message.author))][3] * 2000) + " to upgrade your soldierlevel!",
                                        color=discord.Color.red())
                    msg.set_author(name="solDomination")
                    msg.set_thumbnail(
                        url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                    await message.channel.send(embed=msg)

            else:
                msg = discord.Embed(title="Error",
                                    description="Create your account first!",
                                    color=discord.Color.red())
                msg.set_author(name="solDomination")
                msg.set_thumbnail(url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                await message.channel.send(embed=msg)

        if message.content.lower() == str(default_call) + 'collect money' or message.content.lower() == str(default_call) + 'cm':
            if findPlayer(str(message.author)) != 'nil':
                try:
                    pinfo = players_playing[findPlayer(str(message.author))]
                    if round(time.time()) - pinfo[1][0] >= 10:
                        if str(message.guild) == "solDomination Official Server":
                            collected = round(pinfo[2] * 100 * pinfo[8] * (1 + pinfo[9] * 0.5) * pinfo[12] * 1.1)
                            if round(time.time() - pinfo[1][0] - 10) > 0:
                                offline = math.ceil((pinfo[2] * 100 * pinfo[8] * (1 + pinfo[9] * 0.5) * pinfo[12] * 1.1 / 1000) * round((time.time() - pinfo[1][0] - 10) / 10))
                                collected += offline
                            players_playing[findPlayer(str(message.author))][5] += collected
                            players_playing[findPlayer(str(message.author))][1][0] = time.time()
                            msg = discord.Embed(title="Collected money!!!",
                                                description="You collected `$" + str(
                                                    collected) + "`! The money consists of the `$" + str(
                                                    offline) + "` that you got from being offline! You also got 10% more money because you did it in our official server! :D",
                                                color=discord.Color.gold())
                            msg.set_author(name="solDomination")
                            msg.set_thumbnail(
                                url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                            await message.channel.send(embed=msg)
                        else:
                            collected = round(pinfo[2] * 100 * pinfo[8] * (1 + pinfo[9] * 0.5) * pinfo[12])
                            if round(time.time() - pinfo[1][0] - 10) > 0:
                                offline = math.ceil((pinfo[2] * 100 * pinfo[8] * (1 + pinfo[9] * 0.5) * pinfo[12] / 100) * round((time.time() - pinfo[1][0] - 10) / 10))
                                collected += offline
                            players_playing[findPlayer(str(message.author))][5] += collected
                            players_playing[findPlayer(str(message.author))][1][0] = time.time()
                            msg = discord.Embed(title="Collected money!!!",
                                                description="You collected `$" + str(
                                                    collected) + "`! The money consists of the `$" + str(offline) + "` that you got from being offline!",
                                                color=discord.Color.gold())
                            msg.set_author(name="solDomination")
                            msg.set_thumbnail(
                                url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                            await message.channel.send(embed=msg)
                    else:
                        msg = discord.Embed(title="Too early",
                                            description="A bit too early now, ***please try again later***",
                                            color=discord.Color.red())
                        msg.set_author(name="solDomination")
                        msg.set_thumbnail(
                            url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                        await message.channel.send(embed=msg)
                except TypeError:
                    players_playing[findPlayer(str(message.author))][1] = [pinfo[1], time.time()]
            else:
                msg = discord.Embed(title="Error",
                                    description="Create your account first!",
                                    color=discord.Color.red())
                msg.set_author(name="solDomination")
                msg.set_thumbnail(
                    url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                await message.channel.send(embed=msg)

        if message.content.startswith(str(default_call) + 'buy soldier '):
            if findPlayer(str(message.author)) != 'nil':
                pinfo = players_playing[findPlayer(str(message.author))]
                chan = str(message.channel)
                entity = 16
                content = str(message.content)
                content += '|'
                output = ""
                while content[entity] != '|':
                    output += str(content[entity])
                    entity += 1
                try:
                    output = int(output)
                except ValueError:
                    await message.channel.send("-Error-")
                if pinfo[5] >= output * 100 and output > 0:
                    if output <= 50000:
                        for i in range(output):
                            if "Direct Message" not in chan and len(pinfo[10]) < 20:
                                if random.randint(1, 1000) == 1:
                                    if random.randint(1, 2) == 1:
                                        players_playing[findPlayer(str(message.author))][10].append("sharp 1")
                                        await message.channel.send("***RARE DROP!** You got a sharp 1 book!*")
                                    else:
                                        players_playing[findPlayer(str(message.author))][10].append("lootin1")
                                        await message.channel.send("***RARE DROP!** You got a lootin1 book!*")
                                elif random.randint(1, 10000) == 1:
                                    if random.randint(1, 2) == 1:
                                        players_playing[findPlayer(str(message.author))][10].append("sharp 2")
                                        await message.channel.send("***VERY RARE DROP!** You got a sharp 2 book!*")
                                    else:
                                        players_playing[findPlayer(str(message.author))][10].append("lootin2")
                                        await message.channel.send("***VERY RARE DROP!** You got a lootin2 book!*")
                                elif random.randint(1, 100000) == 1:
                                    if random.randint(1, 2) == 1:
                                        players_playing[findPlayer(str(message.author))][10].append("sharp 3")
                                        await message.channel.send("***SUPER RARE DROP!** You got a sharp 3 book!*")
                                    else:
                                        players_playing[findPlayer(str(message.author))][10].append("lootin3")
                                        await message.channel.send("***SUPER RARE DROP!** You got a lootin3 book!*")
                                elif random.randint(1, 1000000) == 1:
                                    if random.randint(1, 2) == 1:
                                        players_playing[findPlayer(str(message.author))][10].append("sharp 4")
                                        await message.channel.send("***MYTHICAL DROP!** You got a sharp 4 book!*")
                                    else:
                                        players_playing[findPlayer(str(message.author))][10].append("lootin4")
                                        await message.channel.send("***MYTHICAL DROP!** You got a lootin4 book!*")
                                elif random.randint(1, 1000000000) == 1:
                                    if random.randint(1, 2) == 1:
                                        players_playing[findPlayer(str(message.author))][10].append("sharp 5")
                                        await message.channel.send("***LEGENDARY DROP!** You got a sharp 5 book!*")
                                    else:
                                        players_playing[findPlayer(str(message.author))][10].append("lootin5")
                                        await message.channel.send("***LEGENDARY DROP!** You got a lootin5 book!*")
                            players_playing[findPlayer(str(message.author))][5] -= 100
                            players_playing[findPlayer(str(message.author))][4] += 1
                        msg = discord.Embed(title="Success!",
                                            description="You bought " + str(output) + " soldiers!",
                                            color=discord.Color.green())
                        msg.set_author(name="solDomination")
                        msg.set_thumbnail(
                            url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                        await message.channel.send(embed=msg)
                    elif output <= 1000000:
                        for i in range(math.floor(output / 100)):
                            if "Direct Message" not in chan and len(pinfo[10]) < 20:
                                if random.randint(1, 1000) == 1:
                                    if random.randint(1, 2) == 1:
                                        players_playing[findPlayer(str(message.author))][10].append("sharp 1")
                                        await message.channel.send("***RARE DROP!** You got a sharp 1 book!*")
                                    else:
                                        players_playing[findPlayer(str(message.author))][10].append("lootin1")
                                        await message.channel.send("***RARE DROP!** You got a lootin1 book!*")
                                elif random.randint(1, 10000) == 1:
                                    if random.randint(1, 2) == 1:
                                        players_playing[findPlayer(str(message.author))][10].append("sharp 2")
                                        await message.channel.send("***VERY RARE DROP!** You got a sharp 2 book!*")
                                    else:
                                        players_playing[findPlayer(str(message.author))][10].append("lootin2")
                                        await message.channel.send("***VERY RARE DROP!** You got a lootin2 book!*")
                                elif random.randint(1, 100000) == 1:
                                    if random.randint(1, 2) == 1:
                                        players_playing[findPlayer(str(message.author))][10].append("sharp 3")
                                        await message.channel.send("***SUPER RARE DROP!** You got a sharp 3 book!*")
                                    else:
                                        players_playing[findPlayer(str(message.author))][10].append("lootin3")
                                        await message.channel.send("***SUPER RARE DROP!** You got a lootin3 book!*")
                                elif random.randint(1, 1000000) == 1:
                                    if random.randint(1, 2) == 1:
                                        players_playing[findPlayer(str(message.author))][10].append("sharp 4")
                                        await message.channel.send("***MYTHICAL DROP!** You got a sharp 4 book!*")
                                    else:
                                        players_playing[findPlayer(str(message.author))][10].append("lootin4")
                                        await message.channel.send("***MYTHICAL DROP!** You got a lootin4 book!*")
                                elif random.randint(1, 1000000000) == 1:
                                    if random.randint(1, 2) == 1:
                                        players_playing[findPlayer(str(message.author))][10].append("sharp 5")
                                        await message.channel.send("***LEGENDARY DROP!** You got a sharp 5 book!*")
                                    else:
                                        players_playing[findPlayer(str(message.author))][10].append("lootin5")
                                        await message.channel.send("***LEGENDARY DROP!** You got a lootin5 book!*")
                            players_playing[findPlayer(str(message.author))][5] -= 10000
                            players_playing[findPlayer(str(message.author))][4] += 100
                        msg = discord.Embed(title="Success!",
                                            description="You bought " + str(math.floor(output / 100) * 100) + " soldiers!",
                                            color=discord.Color.green())
                        msg.set_author(name="solDomination")
                        msg.set_thumbnail(
                            url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                        await message.channel.send(embed=msg)
                    else:
                        for i in range(math.floor(output / 2500)):
                            if "Direct Message" not in chan and len(pinfo[10]) < 20:
                                if random.randint(1, 1000) == 1:
                                    if random.randint(1, 2) == 1:
                                        players_playing[findPlayer(str(message.author))][10].append("sharp 1")
                                        await message.channel.send("***RARE DROP!** You got a sharp 1 book!*")
                                    else:
                                        players_playing[findPlayer(str(message.author))][10].append("lootin1")
                                        await message.channel.send("***RARE DROP!** You got a lootin1 book!*")
                                elif random.randint(1, 10000) == 1:
                                    if random.randint(1, 2) == 1:
                                        players_playing[findPlayer(str(message.author))][10].append("sharp 2")
                                        await message.channel.send("***VERY RARE DROP!** You got a sharp 2 book!*")
                                    else:
                                        players_playing[findPlayer(str(message.author))][10].append("lootin2")
                                        await message.channel.send("***VERY RARE DROP!** You got a lootin2 book!*")
                                elif random.randint(1, 100000) == 1:
                                    if random.randint(1, 2) == 1:
                                        players_playing[findPlayer(str(message.author))][10].append("sharp 3")
                                        await message.channel.send("***SUPER RARE DROP!** You got a sharp 3 book!*")
                                    else:
                                        players_playing[findPlayer(str(message.author))][10].append("lootin3")
                                        await message.channel.send("***SUPER RARE DROP!** You got a lootin3 book!*")
                                elif random.randint(1, 1000000) == 1:
                                    if random.randint(1, 2) == 1:
                                        players_playing[findPlayer(str(message.author))][10].append("sharp 4")
                                        await message.channel.send("***MYTHICAL DROP!** You got a sharp 4 book!*")
                                    else:
                                        players_playing[findPlayer(str(message.author))][10].append("lootin4")
                                        await message.channel.send("***MYTHICAL DROP!** You got a lootin4 book!*")
                                elif random.randint(1, 1000000000) == 1:
                                    if random.randint(1, 2) == 1:
                                        players_playing[findPlayer(str(message.author))][10].append("sharp 5")
                                        await message.channel.send("***LEGENDARY DROP!** You got a sharp 5 book!*")
                                    else:
                                        players_playing[findPlayer(str(message.author))][10].append("lootin5")
                                        await message.channel.send("***LEGENDARY DROP!** You got a lootin5 book!*")
                            players_playing[findPlayer(str(message.author))][5] -= 250000
                            players_playing[findPlayer(str(message.author))][4] += 2500
                        msg = discord.Embed(title="Success!",
                                            description="You bought " + str(math.floor(output / 2500) * 2500) + " soldiers!",
                                            color=discord.Color.green())
                        msg.set_author(name="solDomination")
                        msg.set_thumbnail(
                            url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                        await message.channel.send(embed=msg)
                else:
                    msg = discord.Embed(title="Error",
                                        description="You do not have enough money! Do take note a soldier cost $100 per",
                                        color=discord.Color.red())
                    msg.set_author(name="solDomination")
                    msg.set_thumbnail(
                        url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                    await message.channel.send(embed=msg)
            else:
                msg = discord.Embed(title="Error",
                                    description="Create your account first!",
                                    color=discord.Color.red())
                msg.set_author(name="solDomination")
                msg.set_thumbnail(
                    url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                await message.channel.send(embed=msg)

        if message.content.startswith(str(default_call) + "use book "):
            pinfo = players_playing[findPlayer(str(message.author))]
            entity = 13
            content = str(message.content)
            content += '|'
            output = ""
            while content[entity] != '|':
                output += str(content[entity])
                entity += 1
            if output in pinfo[10]:
                for i in range(len(pinfo[10])):
                    if pinfo[10][i] == output:
                        if str(pinfo[10][i])[0] == "l":
                            players_playing[findPlayer(str(message.author))][12] = 1
                            players_playing[findPlayer(str(message.author))][12] += int(output[6]) / 10
                            players_playing[findPlayer(str(message.author))][10].pop(i)
                            msg = discord.Embed(title="Book used!",
                                                description="You used your Looting " + str(output[6]) + " book!",
                                                color=discord.Color.green())
                            msg.set_author(name="solDomination")
                            msg.set_thumbnail(
                                url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                            await message.channel.send(embed=msg)
                            break
                        elif str(pinfo[10][i])[0] == "s":
                            players_playing[findPlayer(str(message.author))][11] = 1
                            players_playing[findPlayer(str(message.author))][11] += int(output[6]) / 5
                            players_playing[findPlayer(str(message.author))][10].pop(i)
                            msg = discord.Embed(title="Book used!",
                                                description="You used your Sharpness " + str(output[6]) + " book!",
                                                color=discord.Color.green())
                            msg.set_author(name="solDomination")
                            msg.set_thumbnail(
                                url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                            await message.channel.send(embed=msg)
                            break
            else:
                msg = discord.Embed(title="Error",
                                    description="You do not have that book",
                                    color=discord.Color.red())
                msg.set_author(name="solDomination")
                msg.set_thumbnail(
                    url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                await message.channel.send(embed=msg)

        if message.content.startswith(str(default_call) + 'info '):
            entity = 9
            content = str(message.content)
            content += '|'
            output = ""
            while content[entity] != '|':
                output += str(content[entity])
                entity += 1
            if findPlayer(output) != 'nil':
                person = players_playing[findPlayer(output)]
                netWorth = person[2] * 1000 + person[3] * 2000 + person[4] * 40
                if len(person) <= 14:
                    if len(person) == 13:
                        players_playing[findPlayer(str(output))].append(0)
                    if len(person) == 14:
                        players_playing[findPlayer(str(output))].append('')
                msg = discord.Embed(title="Info",
                                    description="Name: " + str(person[0]) + "\nBankLevel: " + str(person[2]) + "\nSoldierLevel: " + str(
                    person[3]) + "\nSoldierAmount: " + str(person[4]) + "\nMoney: $" + str(
                    person[5]) + "\nInsta-cash: " + str(person[6]) + "\nGems: " + str(person[13]) + "\nNukes: " + str(person[7][1]) + "\nCoal: " + str(
                    person[7][0]) + "\nMultiplier: " + str(person[8]) + "\nRebirths: " + str(person[9]) + "\nNetworth: $" +
                    str(netWorth) + "\nSharpness Multiplier: " + str(person[11]) + "x\nLooting Multiplier: " + str(person[12]) + "x\nRebirth Multiplier: " + str(1 + (person[9] * 0.5)) + "x\nBooks: " + str(person[10]) + "\nGuild: " + str(person[14]),
                                    color=discord.Color.blue())
                msg.set_author(name="solDomination")
                msg.set_thumbnail(
                    url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                await message.channel.send(embed=msg)
            else:
                msg = discord.Embed(title="Error",
                                    description="Player not found",
                                    color=discord.Color.red())
                msg.set_author(name="solDomination")
                msg.set_thumbnail(
                    url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                await message.channel.send(embed=msg)

        if message.content.lower() == str(default_call) + "info":
            if findPlayer(str(message.author)) != 'nil':
                person = players_playing[findPlayer(str(message.author))]
                netWorth = person[2] * 1000 + person[3] * 2000 + person[4] * 40
                msg = discord.Embed(title="Info",
                                    description="Name: " + str(person[0]) + "\nBankLevel: " + str(
                                        person[2]) + "\nSoldierLevel: " + str(
                                        person[3]) + "\nSoldierAmount: " + str(person[4]) + "\nMoney: $" + str(
                                        person[5]) + "\nInsta-cash: " + str(person[6]) + "\nGems: " + str(
                                        person[13]) + "\nNukes: " + str(person[7][1]) + "\nCoal: " + str(
                                        person[7][0]) + "\nMultiplier: " + str(person[8]) + "\nRebirths: " + str(
                                        person[9]) + "\nNetworth: $" +
                                                str(netWorth) + "\nSharpness Multiplier: " + str(
                                        person[11]) + "x\nLooting Multiplier: " + str(
                                        person[12]) + "x\nRebirth Multiplier: " + str(
                                        1 + (person[9] * 0.5)) + "x\nGuild: " + str(
                                        person[14]),
                                    color=discord.Color.blue())
                msg.set_author(name="solDomination")
                msg.set_thumbnail(
                    url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                await message.channel.send(embed=msg)
            else:
                msg = discord.Embed(title="Error",
                                    description="Create your account first!",
                                    color=discord.Color.red())
                msg.set_author(name="solDomination")
                msg.set_thumbnail(
                    url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                await message.channel.send(embed=msg)

        if message.content.startswith(str(default_call) + 'give '):
            if message.content.startswith(str(default_call) + 'give insta-cash '):
                if str(message.author) in authorised:
                    entity = 20
                    content = str(message.content)
                    content += '|'
                    output = ['', '']
                    while content[entity] != '|':
                        output[0] += str(content[entity])
                        entity += 1
                    entity += 1
                    while content[entity] != '|':
                        output[1] += str(content[entity])
                        entity += 1
                    try:
                        players_playing[findPlayer(str(output[0]))][6] += int(output[1])
                        await message.channel.send("```Successfully added " + str(output[1]) + " insta-cash into " + str(output[0]) + "'s account!```")
                        msg = discord.Embed(title="Success!",
                                            description="```Successfully added " + str(output[1]) + " insta-cash into " + str(output[0]) + "'s account!```",
                                            color=discord.Color.green())
                        msg.set_author(name="solDomination")
                        msg.set_thumbnail(
                            url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                        await message.channel.send(embed=msg)
                        user = client.get_user(603569154171207701)
                        await user.send("<@!603569154171207701> " + str(message.author) + " gave " + str(output[1]) + " insta-cash to " + str(output[0]))
                    except:
                        msg = discord.Embed(title="Error",
                                            description="An error has occurred",
                                            color=discord.Color.red())
                        msg.set_author(name="solDomination")
                        msg.set_thumbnail(
                            url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                        await message.channel.send(embed=msg)
                else:
                    msg = discord.Embed(title="Error",
                                        description=str(message.author.mention) + ", you do not have the authority to do that",
                                        color=discord.Color.red())
                    msg.set_author(name="solDomination")
                    msg.set_thumbnail(
                        url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                    await message.channel.send(embed=msg)
            if message.content.startswith(str(default_call) + 'give money '):
                if str(message.author) in authorised:
                    entity = 15
                    content = str(message.content)
                    content += '|'
                    output = ['', '']
                    while content[entity] != '|':
                        print(content[entity])
                        output[0] += str(content[entity])
                        entity += 1
                    entity += 1
                    while content[entity] != '|':
                        output[1] += str(content[entity])
                        entity += 1
                    try:
                        players_playing[findPlayer(str(output[0]))][5] += int(output[1])
                        msg = discord.Embed(title="Success!",
                                            description="```Successfully added $" + str(
                                                output[1]) + " into " + str(output[0]) + "'s account!```",
                                            color=discord.Color.green())
                        msg.set_author(name="solDomination")
                        msg.set_thumbnail(
                            url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                        await message.channel.send(embed=msg)
                        user = client.get_user(603569154171207701)
                        await user.send(
                            "<@!603569154171207701> " + str(message.author) + " gave $" + str(output[1]) + " to " + str(
                                output[0]))
                    except IndexError:
                        msg = discord.Embed(title="Error",
                                            description="An error has occurred",
                                            color=discord.Color.red())
                        msg.set_author(name="solDomination")
                        msg.set_thumbnail(
                            url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                        await message.channel.send(embed=msg)
                else:
                    msg = discord.Embed(title="Error",
                                        description=", you do not have the authority to do that",
                                        color=discord.Color.red())
                    msg.set_author(name="solDomination")
                    msg.set_thumbnail(
                        url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                    await message.channel.send(embed=msg)

        if message.content.startswith(str(default_call) + 'use insta-cash '):
            if findPlayer(str(message.author)) != 'nil':
                pinfo = players_playing[findPlayer(str(message.author))]
                if players_playing[findPlayer(str(message.author))][4] != 0:
                    entity = 19
                    content = str(message.content)
                    content += '|'
                    output = ''
                    while content[entity] != '|':
                        print(content[entity])
                        output += str(content[entity])
                        entity += 1
                    print(output)
                    try:
                        output = int(output)
                        if output <= 0:
                            raise ValueError
                    except ValueError:
                        msg = discord.Embed(title="Error",
                                            description="An error has occurred",
                                            color=discord.Color.red())
                        msg.set_author(name="solDomination")
                        msg.set_thumbnail(
                            url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                        await message.channel.send(embed=msg)
                        return
                    if pinfo[6] >= output:
                        for i in range(output):
                            players_playing[findPlayer(str(message.author))][5] += pinfo[2] * 100 * (1 + pinfo[9] * 0.5) * pinfo[8]
                            players_playing[findPlayer(str(message.author))][6] -= 1
                            if random.randint(1, 100) == 1:
                                players_playing[findPlayer(str(message.author))][13] += 1
                                await message.channel.send("```VERY LUCKY DROP! YOU GOT 1 GEM!```")
                                msg = discord.Embed(title="OOG!",
                                                    description="YOU GOT 1 GEM!!! AMAZING!",
                                                    color=discord.Color.dark_grey())
                                msg.set_author(name="solDomination")
                                msg.set_thumbnail(
                                    url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                                await message.channel.send(embed=msg)
                        msg = discord.Embed(title="Success!",
                                            description="You used " + str(output) + " insta-cash!",
                                            color=discord.Color.green())
                        msg.set_author(name="solDomination")
                        msg.set_thumbnail(
                            url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                        await message.channel.send(embed=msg)
                    else:
                        msg = discord.Embed(title="Error",
                                            description="You do not have enough insta-cash!",
                                            color=discord.Color.red())
                        msg.set_author(name="solDomination")
                        msg.set_thumbnail(
                            url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                        await message.channel.send(embed=msg)
                else:
                    msg = discord.Embed(title="Error",
                                        description="You cannot use insta-cash while in passive! Get out of passive by buying a soldier!",
                                        color=discord.Color.red())
                    msg.set_author(name="solDomination")
                    msg.set_thumbnail(
                        url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                    await message.channel.send(embed=msg)
            else:
                msg = discord.Embed(title="Error",
                                    description="Create your account first!",
                                    color=discord.Color.red())
                msg.set_author(name="solDomination")
                msg.set_thumbnail(
                    url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                await message.channel.send(embed=msg)

        if message.content.startswith(str(default_call) + 'raid '):
            if players_playing[findPlayer(str(message.author))] != 'nil':
                entity = 9
                content = str(message.content)
                content += '|'
                output = ''
                while content[entity] != '|':
                    output += str(content[entity])
                    entity += 1
                print(output)
                pinfo = players_playing[findPlayer(str(message.author))]
                if str(message.author) != str(output):
                    if findPlayer(output) != 'nil':
                        phiminfo = players_playing[findPlayer(output)]
                        netWorth = phiminfo[2] * 1000 + phiminfo[3] * 2000 + phiminfo[4] * 40
                        soldierpower = round(phiminfo[3] * phiminfo[4] * phiminfo[11] * (1 + phiminfo[9] * 0.5))
                        mysp = round(pinfo[3] * pinfo[4] * pinfo[11] * (1 + pinfo[9] * 0.5))
                        if guildFind(pinfo[14]) != 'nil':
                            if output not in guilds[guildFind(pinfo[14])]:
                                if lpassiveFind(str(phiminfo[0])) == 'nil':
                                    if soldierpower > 0:
                                        if random.randint(int(soldierpower / 4), int(soldierpower)) <= int(mysp):
                                            y = pinfo[5]
                                            players_playing[findPlayer(str(message.author))][6] += phiminfo[6]
                                            players_playing[findPlayer(str(message.author))][5] += (netWorth + phiminfo[5]) * (1 + pinfo[9] * 0.5) * pinfo[12]
                                            x = round(soldierpower / pinfo[3])
                                            print("netWorth: " + str(netWorth))
                                            if x > pinfo[4]:
                                                x = pinfo[4]
                                                players_playing[findPlayer(str(message.author))][4] = 0
                                            else:
                                                players_playing[findPlayer(str(message.author))][4] -= x
                                            msg = discord.Embed(title="YAY!",
                                                                description="Woohoo! You got a successful raid! You managed to get $" + str(players_playing[findPlayer(str(message.author))][5] - y) + " and " + str(phiminfo[6]) + " insta-cash! However, you lost " + str(x) + " amount of troops :(",
                                                                color=discord.Color.green())
                                            msg.set_author(name="solDomination")
                                            msg.set_thumbnail(
                                                url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                                            await message.channel.send(embed=msg)
                                            user = client.get_user(603569154171207701)
                                            await user.send(str(message.author) + " raided " + str(output))
                                            players_playing[findPlayer(output)] = [output, [round(time.time()), round(time.time())], 1, 1, 0, 0, 0, [0, 0], 1, phiminfo[9], phiminfo[10], phiminfo[11], phiminfo[12], phiminfo[13], phiminfo[14]]
                                        else:
                                            players_playing[findPlayer(str(message.author))][4] = 0
                                            players_playing[findPlayer(str(message.author))][5] = 0
                                            msg = discord.Embed(title="OOF!",
                                                                description="You failed the raid!",
                                                                color=discord.Color.red())
                                            msg.set_author(name="solDomination")
                                            msg.set_thumbnail(
                                                url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                                            await message.channel.send(embed=msg)
                                    else:
                                        msg = discord.Embed(title="Error",
                                                            description="That player is in passive, don't irritate him",
                                                            color=discord.Color.red())
                                        msg.set_author(name="solDomination")
                                        msg.set_thumbnail(
                                            url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                                        await message.channel.send(embed=msg)
                                else:
                                    msg = discord.Embed(title="Error",
                                                        description="Your opponent has a shield, so you cannot raid him",
                                                        color=discord.Color.red())
                                    msg.set_author(name="solDomination")
                                    msg.set_thumbnail(
                                        url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                                    await message.channel.send(embed=msg)
                            else:
                                msg = discord.Embed(title="Error",
                                                    description="You cannot raid your guild mate!",
                                                    color=discord.Color.red())
                                msg.set_author(name="solDomination")
                                msg.set_thumbnail(
                                    url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                                await message.channel.send(embed=msg)
                        else:
                            if lpassiveFind(str(phiminfo[0])) == 'nil':
                                if soldierpower > 0:
                                    if random.randint(int(soldierpower / 4), int(soldierpower)) <= int(mysp):
                                        y = pinfo[5]
                                        players_playing[findPlayer(str(message.author))][6] += phiminfo[6]
                                        players_playing[findPlayer(str(message.author))][5] += (netWorth + phiminfo[5]) * (1 + pinfo[9] * 0.5) * pinfo[12]
                                        x = round(soldierpower / pinfo[3])
                                        print("netWorth: " + str(netWorth))
                                        if x > pinfo[4]:
                                            x = pinfo[4]
                                            players_playing[findPlayer(str(message.author))][4] = 0
                                        else:
                                            players_playing[findPlayer(str(message.author))][4] -= x
                                        msg = discord.Embed(title="YAY!",
                                                            description="Woohoo! You got a successful raid! You managed to get $" + str(
                                                                players_playing[findPlayer(str(message.author))][
                                                                    5] - y) + " and " + str(
                                                                phiminfo[6]) + " insta-cash! However, you lost " + str(
                                                                x) + " amount of troops :(",
                                                            color=discord.Color.green())
                                        msg.set_author(name="solDomination")
                                        msg.set_thumbnail(
                                            url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                                        await message.channel.send(embed=msg)
                                        user = client.get_user(603569154171207701)
                                        await user.send(str(message.author) + " raided " + str(output))
                                        players_playing[findPlayer(output)] = [output, round(time.time()), 1, 1, 0, 0, 0, [0, 0], 1, phiminfo[9], phiminfo[10], phiminfo[11], phiminfo[12], phiminfo[13], phiminfo[14]]
                                    else:
                                        players_playing[findPlayer(str(message.author))][4] = 0
                                        players_playing[findPlayer(str(message.author))][5] = 0
                                        msg = discord.Embed(title="OOF!",
                                                            description="You failed the raid!",
                                                            color=discord.Color.red())
                                        msg.set_author(name="solDomination")
                                        msg.set_thumbnail(
                                            url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                                        await message.channel.send(embed=msg)
                                else:
                                    msg = discord.Embed(title="Error",
                                                        description="That player is in passive, don't irritate him",
                                                        color=discord.Color.red())
                                    msg.set_author(name="solDomination")
                                    msg.set_thumbnail(
                                        url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                                    await message.channel.send(embed=msg)
                            else:
                                msg = discord.Embed(title="Error",
                                                    description="Your opponent has a shield, so you cannot raid him",
                                                    color=discord.Color.red())
                                msg.set_author(name="solDomination")
                                msg.set_thumbnail(
                                    url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                                await message.channel.send(embed=msg)
                    else:
                        msg = discord.Embed(title="Error",
                                            description="That player does not play solDomination!",
                                            color=discord.Color.red())
                        msg.set_author(name="solDomination")
                        msg.set_thumbnail(
                            url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                        await message.channel.send(embed=msg)
                else:
                    msg = discord.Embed(title="Error",
                                        description="Why are you trying to raid yourself?",
                                        color=discord.Color.red())
                    msg.set_author(name="solDomination")
                    msg.set_thumbnail(
                        url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                    await message.channel.send(embed=msg)
            else:
                msg = discord.Embed(title="Error",
                                    description="Create your account first!",
                                    color=discord.Color.red())
                msg.set_author(name="solDomination")
                msg.set_thumbnail(
                    url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                await message.channel.send(embed=msg)

        if message.content.startswith(str(default_call) + 'share '):
            if players_playing[findPlayer(str(message.author))] != 'nil':
                pinfo = players_playing[findPlayer(str(message.author))]
                entity = 10
                content = str(message.content)
                content += '|'
                output = ['', '', '']
                while content[entity] != '|':
                    output[0] += str(content[entity])
                    entity += 1
                entity += 1
                while content[entity] != '|':
                    output[1] += str(content[entity])
                    entity += 1
                entity += 1
                while content[entity] != '|':
                    output[2] += str(content[entity])
                    entity += 1
                if findPlayer(output[0]) != 'nil':
                    if output[2] == "money":
                        output[1] = int(output[1])
                        if pinfo[5] >= output[1] and output[1] > 0:
                            players_playing[findPlayer(output[0])][5] += output[1]
                            players_playing[findPlayer(str(message.author))][5] -= output[1]
                            msg = discord.Embed(title="Success transaction!",
                                                description="You transected $" + str(output[1]) + " to " + str(output[0]) + "!",
                                                color=discord.Color.green())
                            msg.set_author(name="solDomination")
                            msg.set_thumbnail(
                                url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                            await message.channel.send(embed=msg)
                        else:
                            msg = discord.Embed(title="Error",
                                                description="You do not have enough money!",
                                                color=discord.Color.red())
                            msg.set_author(name="solDomination")
                            msg.set_thumbnail(
                                url="https://lh3.googleusercontent.com/-vXIpYDFA3e0/XyEfzBR93VI/AAAAAAAABVw/caO_Hp9wE3w1Uq5KL7cfBl-xwDBH7LyvACK8BGAsYHg/s0/2020-07-29.png")
                            await message.channel.send(embed=msg)
                    if output[2] == "insta-cash":
                        output[1] = int(output[1])
                        if pinfo[6] >= output[1] and output[1] > 0:
                            players_playing[findPlayer(output[0])][6] += output[1]
                            players_playing[findPlayer(str(message.author))][6] -= output[1]
                            await message.channel.send("```Success transaction! You transected " + str(output[1]) + " insta-cash to " + str(output[0]) + '!```')
                        else:
                            await message.channel.send("```Not enough insta-cash!```")
                    if output[2] == "book":
                        if str(output[1]) in pinfo[10]:
                            for i in range(len(pinfo[10])):
                                if pinfo[10][i] == str(output[1]):
                                    players_playing[findPlayer(output[0])][10].append(str(output[1]))
                                    players_playing[findPlayer(str(message.author))][10].pop(i)
                                    break
                            await message.channel.send("```Success transaction! You transected " + str(output[1]) + " book to " + str(output[0]) + '!```')
                        else:
                            await message.channel.send("```You don't have that book!```")
                else:
                    await message.channel.send("```Who's that???```")
            else:
                await message.channel.send("```Create an account first!```")

        if message.content.lower() == str(default_call) + 'help':
            await message.channel.send("```Commands:```" + "```sol start --> Starts your profile```" + "```sol collect money --> Collect the money your bank produced```" + "```sol upgrade bank --> Upgrades the bank output of $ per 10s(It costs CurrentBankLevel * 1000)```" + "```sol upgrade soldier --> Upgrades your soldier, making them stronger(It costs CurrentSoldierLevel * 2000)```" + "```sol raid <person> --> RAIDS SOMEONE```" + "```sol info <person> --> Views <person> stats```" + "```sol use insta-cash <amt> --> Uses insta-cash```" + '```sol use coal <amt> --> Uses coal(coal gives +0.1x more money)```' + "```sol shop --> Views the fuel shop```" + "```sol rebirth --> Rebirths(You need to have 100000 * RebirthAmt of networth in order to rebirth)```" + "```sol books --> Views the books you currently have```" + "```sol use book <book> --> Uses a book```" + "```sol soldierpower --> Views your soldier power```" + "```sol nuke <player> --> Nuke someone with a nuke(nukes are in the shop)```" + "```sol coinflip <amt>|<heads/tails> --> Coinflips```" + "```sol share <person>|<amount/item_name>|<item-type> --> Shares an item with somebody```" + "```sol buy shield--> Buys a shield(costs 1/10of your total netWorth)```" + "```sol search --> search for items```" + "```sol prestige --> Prestige and get gems(req. at least 25 rebirths to do so)!```" + "```sol gem_shop --> View the gem shop```" + "```sol dungeon create --> Create dungeon```" + "```sol dungeon start --> Start dungeon```" + "```sol dungeon join <name> --> Join someone's dungeon```")

        if message.content.lower() == str(default_call) + 'shop':
            lust = players_playing[findPlayer(str(message.author))]
            cost = round((2 ** (lust[7][0] + ((lust[8] - 1) / 0.1))) * 500)
            await message.channel.send("```Please do \"sol buy <item>\" to buy an item from the shop(Please state your amount at the end if you are buying soldiers)``````Soldier: $100``````Coal (Increases output by 10%): $" + str(cost) + "(doubles per coal you buy and is different for each person)``````Nuke: $1000000(Destroys 90% of your enemy's soldier's)```")

        if message.content.lower() == str(default_call) + 'buy nuke':
            if findPlayer(str(message.author)) != 'nil':
                pinfo = players_playing[findPlayer(str(message.author))]
                if pinfo[5] >= 1000000:
                    if len(pinfo[7]) < 2:
                        players_playing[findPlayer(str(message.author))][7].append(1)
                    else:
                        players_playing[findPlayer(str(message.author))][7][1] += 1
                    players_playing[findPlayer(str(message.author))][5] -= 1000000
                    await message.channel.send("```You bought a nuke! You can use a nuke by doing \"sol nuke <player>\"```")
                else:
                    await message.channel.send("```Not enough money!```")
            else:
                await message.channel.send("```Create an account first!```")

        if message.content.startswith(str(default_call) + 'nuke '):
            if findPlayer(str(message.author)) != 'nil':
                output = ""
                entity = 9
                content = str(message.content)
                content += '|'
                while content[entity] != '|':
                    output += str(content[entity])
                    entity += 1
                if findPlayer(output) != 'nil':
                    if players_playing[findPlayer(str(message.author))][7][1] > 0:
                        phiminfo = players_playing[findPlayer(output)]
                        players_playing[findPlayer(str(message.author))][7][1] -= 1
                        players_playing[findPlayer(output)][4] = round(phiminfo[4] / 10)
                        await message.channel.send("Success nuke! You managed to explode away " + str(9 * phiminfo[4]) + " soldiers from " + str(output) + "!")
                    else:
                        await message.channel.send("```You have no nukes!```")
                else:
                    await message.channel.send("```Who is that???```")
            else:
                await message.channel.send("```Create an account first```")

        if message.content.lower() == str(default_call) + 'buy coal':
            if findPlayer(str(message.author)) != 'nil':
                lust = players_playing[findPlayer(str(message.author))]
                cost = round((2 ** (lust[7][0] + ((lust[8] - 1) / 0.1))) * 500)
                if lust[5] >= cost:
                    players_playing[findPlayer(str(message.author))][7][0] += 1
                    players_playing[findPlayer(str(message.author))][5] -= cost
                    cost = round((2 ** (lust[7][0] + ((lust[8] - 1) / 0.1))) * 500)
                    await message.channel.send("```Successfully bought 1 coal!```")
                else:
                    await message.channel.send("```Not Enough Money!```")
            else:
                await message.channel.send("```Create an account first!```")

        if message.content.startswith(str(default_call) + 'use coal '):
            if findPlayer(str(message.author)) != 'nil':
                if players_playing[findPlayer(str(message.author))][7][0] > 0:
                    entity = 12
                    content = str(message.content)
                    content += '|'
                    output = ''
                    while content[entity] != '|':
                        output += str(content[entity])
                        entity += 1
                    try:
                        output = int(output)
                    except:
                        await message.channel.send("```-Error-```")
                    if players_playing[findPlayer(str(message.author))][7][0] >= output and not output <= 0:
                        players_playing[findPlayer(str(message.author))][8] += 0.1 * output
                        players_playing[findPlayer(str(message.author))][7][0] -= output
                        print(players_playing[findPlayer(str(message.author))])
                        await message.channel.send("```You used " + str(output) + " coal!```")
                    else:
                        await message.channel.send("```You do not have enough coal!```")
                else:
                    await message.channel.send("```You have no coal, you loser```")
            else:
                await message.channel.send("```Create an account first!```")

        if message.content.lower() == str(default_call) + 'members_playing':
            await message.channel.send("```People who play Domination: " + str(len(players_playing)) + "```")

        if message.content.lower() == str(default_call) + "rebirth" or message.content.lower() == str(default_call) + "rb":
            if findPlayer(str(message.author)) != 'nil':
                pinfo = players_playing[findPlayer(str(message.author))]
                netWorth = pinfo[2] * 1000 + pinfo[3] * 2000 + pinfo[4] * 40
                if netWorth >= (pinfo[9] + 1) * 100000:
                    players_playing[findPlayer(str(message.author))] = [str(message.author), [round(time.time()), round(time.time())], 1, 1, 0, 0, 0, [0, 0], 1, pinfo[9] + 1, pinfo[10], pinfo[11], pinfo[12], pinfo[13], pinfo[14]]
                    await message.channel.send("```You rebirthed!```")
                else:
                    await message.channel.send("```You do not have enough networth, " + str(message.author) + "! You only have a networth of $" + str(netWorth) + ", and you need a netWorth of $" +
                                               str((pinfo[9] + 1) * 100000) + " to rebirth!```")
            else:
                await message.channel.send("```Create your account first!```")

        if message.content.lower() == str(default_call) + "prestige" or message.content.lower() == str(default_call) + "pr":
            if findPlayer(str(message.author)) != 'nil':
                pinfo = players_playing[findPlayer(str(message.author))]
                if pinfo[9] >= 25:
                    num = random.randint(3, 5)
                    players_playing[findPlayer(str(message.author))] = [str(message.author), [round(time.time()), round(time.time())], 1, 1, 0, 0, 0, [0, 0], 1, 0, [], 1, 1, pinfo[13] + num, pinfo[14]]
                    await message.channel.send("```You prestiged and got" + str(num) + " gems!```")
                else:
                    await message.channel.send("```You do not have enough rebirths, " + str(message.author) + "! You only have " + str(pinfo[9]) + " rebirths, and you need 25 rebirths to prestige!```")
            else:
                await message.channel.send("```Create your account first!```")

        if message.content.lower() == str(default_call) + "books":
            if findPlayer(str(message.author)) != 'nil':
                try:
                    pinfo = players_playing[findPlayer(str(message.author))]
                    show = ""
                    for i in range(len(pinfo[10])):
                        show += "```" + str(pinfo[10][i]) + "```"
                    await message.channel.send(str(show))
                except discord.errors.HTTPException:
                    await message.channel.send("```You have no books!```")
            else:
                await message.channel.send("```Create your account first!```")

        if message.content.lower() == str(default_call) + "sp" or message.content == str(default_call) + "soldierpower":
            if findPlayer(str(message.author)) != 'nil':
                pinfo = players_playing[findPlayer(str(message.author))]
                soldierpower = round(pinfo[3] * pinfo[4] * pinfo[11] * (1 + pinfo[9] * 0.5))
                await message.channel.send("```Your soldier power is: " + str(soldierpower) + "```")
            else:
                await message.channel.send("```Create your account first!```")

        if message.content.lower() == str(default_call) + "last-checked" or message.content.lower() == str(default_call) + "lc":
            if findPlayer(str(message.author)) != 'nil':
                seconds = time.time() - players_playing[findPlayer(str(message.author))][1]
                days = math.floor(seconds / 86400)
                hours = math.floor((seconds % 86400) / 3600)
                minutes = math.floor(((seconds % 86400) % 3600) / 60)
                seconds = math.floor(((seconds % 86400) % 3600) % 60)
                await message.channel.send("```You last collected " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes and " + str(seconds) + " seconds ago.```")
            else:
                await message.channel.send("```Create your account first!```")

        if message.content.startswith(str(default_call) + "lc "):
            if findPlayer(str(message.author)) != 'nil':
                entity = 7
                content = str(message.content)
                content += '|'
                output = ''
                while content[entity] != '|':
                    output += str(content[entity])
                    entity += 1
                if findPlayer(output) != 'nil':
                    seconds = time.time() - players_playing[findPlayer(str(output))][1]
                    days = math.floor(seconds / 86400)
                    hours = math.floor((seconds % 86400) / 3600)
                    minutes = math.floor(((seconds % 86400) % 3600) / 60)
                    seconds = math.floor(((seconds % 86400) % 3600) % 60)
                    await message.channel.send("```" + str(output) + " last collected " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes and " + str(seconds) + " seconds ago.```")
                else:
                    await message.channel.send("Who's that???")
            else:
                await message.channel.send("```Create your account first!```")

        if message.content.lower() == str(default_call) + "invite":
            await message.channel.send("To invite my bot to your server, open this link: `https://discord.com/api/oauth2/authorize?client_id=720906801607999579&permissions=523328&scope=bot`")

        if message.content.startswith(str(default_call) + "modKick "):
            if str(message.author) in authorised:
                entity = 12
                content = str(message.content)
                content += '|'
                output = ''
                while content[entity] != '|':
                    output += str(content[entity])
                    entity += 1
                if findPlayer(output) != 'nil':
                    players_playing.pop(findPlayer(output))
                    await message.channel.send("Removed `" + str(output) + "`'s account from the game!")
                else:
                    await message.channel.send("Who is that???")
            else:
                await message.channel.send("You do not have the authority to do that!")

        if message.content.startswith(str(default_call) + "coinflip "):
            if findPlayer(str(message.author)) != 'nil':
                pinfo = players_playing[findPlayer(str(message.author))]
                entity = 13
                content = str(message.content)
                content += '|'
                output = ['', '']
                while content[entity] != '|':
                    output[0] += str(content[entity])
                    entity += 1
                entity += 1
                while content[entity] != '|':
                    output[1] += str(content[entity])
                    entity += 1
                try:
                    output[0] = int(output[0])
                    if output[0] > 0:
                        if pinfo[5] >= output[0]:
                            if output[1] == 'heads' or output[1] == 'head':
                                if random.randint(1, 2) == 1:
                                    players_playing[findPlayer(str(message.author))][5] += output[0]
                                    await message.channel.send("```You won the flip! You got $" + str(output[0]) + "!```")
                                else:
                                    players_playing[findPlayer(str(message.author))][5] -= output[0]
                                    await message.channel.send("```You lost the flip... you lost $" + str(output[0]) + "!```")
                            elif output[1] == 'tails' or output[1] == 'tail':
                                if random.randint(1, 2) == 2:
                                    players_playing[findPlayer(str(message.author))][5] += output[0]
                                    await message.channel.send("```You won the flip! You got $" + str(output[0]) + "!```")
                                else:
                                    players_playing[findPlayer(str(message.author))][5] -= output[0]
                                    await message.channel.send("```You lost the flip... you lost $" + str(output[0]) + "!```")
                            else:
                                await message.channel.send("```Please enter a valid bidding on a side; heads or tails```")
                        else:
                            await message.channel.send("```Not enough money!```")
                    else:
                        await message.channel.send("Enter a number more than 0!")
                except ValueError:
                    await message.channel.send("```Please enter in a valid number to bet, " + str(message.author) + "```")
            else:
                await message.channel.send("```Create your account first!```")

        if message.content.lower() == str(default_call) + "rules":
            await message.channel.send("```Breaking any of these rules will result in a kick/ban``````Rule #1: Do not macro commands``````Rule #2: Do not spam for events```")

        if message.content.lower() == str(default_call) + "buy shield":
            if findPlayer(str(message.author)) != 'nil':
                if len(passive) <= 500:
                    pinfo = players_playing[findPlayer(str(message.author))]
                    netWorth = pinfo[2] * 1000 + pinfo[3] * 2000 + pinfo[4] * 40
                    if pinfo[5] >= netWorth / 10:
                        if lpassiveFind(str(message.author)) != 'nil':
                            passive[lpassiveFind(str(message.author))][1] += 1
                        else:
                            passive.append([str(message.author), 1, time.time()])
                        await message.channel.send("```You got a shield!```")
                    else:
                        await message.channel.send("```You have no money!```")
                else:
                    await message.channel.send("```Sorry, too many people have shields currently so nobody is allowed to buy one```")
            else:
                await message.channel.send("```Create your account first!```")

        if message.content.lower() == str(default_call) + "ut" and str(message.author) in authorised:
            if not updating:
                updating = True
                await message.channel.send("`Nobody can access the bot now!`")
            else:
                await message.channel.send("`Updating mode is already enabled!`")

        if message.content.lower() == str(default_call) + "uf" and str(message.author) in authorised:
            if updating:
                updating = False
                await message.channel.send("`People are now re-allowed to access the bot!`")
            else:
                await message.channel.send("`Updating mode is already disabled!`")

        if message.content.lower() == str(default_call) + "search":
            if findPlayer(str(message.author)) != 'nil':
                pinfo = players_playing[findPlayer(str(message.author))]
                if pinfo[4] >= 250:
                    if random.randint(1, 5) == 1:
                        num = round(random.randint(pinfo[2] * 200, pinfo[2] * 1500))
                        players_playing[findPlayer(str(message.author))][5] += num
                        await message.channel.send("```You got $" + str(num) + "!```")
                        return
                    elif random.randint(1, 7) == 1:
                        num = random.randint(10, 20)
                        players_playing[findPlayer(str(message.author))][6] += num
                        await message.channel.send("```You got " + str(num) + " insta-cash!```")
                        return
                    else:
                        try:
                            num = round(random.randint(round(pinfo[4] / 2), pinfo[4] - 1))
                            players_playing[findPlayer(str(message.author))][4] -= num
                            await message.channel.send("```OOF, you got nothing and lost " + str(num) + " soldiers!```")
                        except ValueError:
                            num = pinfo[4]
                            players_playing[findPlayer(str(message.author))][4] = 0
                            await message.channel.send("```OOF, you got nothing and lost " + str(num) + " soldiers!```")
                else:
                    await message.channel.send("```You need at least 250 soldiers to search!```")
            else:
                await message.channel.send("```Create an account first!```")

        if message.content.lower() == str(default_call) + "gem_shop":
            if findPlayer(str(message.author)) != 'nil':
                if len(offers) != 0:
                    pass
                    txt = '```Please do "sol buy pack <index>" to buy a pack``````Offers:```'
                    for i in range(len(offers)):
                        txt += "```Pack " + str(i + 1) + ":```"
                        txt += "```    Coins: " + str(offers[i][0]) + "```"
                        txt += "```    Coal: " + str(offers[i][1]) + "```"
                        txt += "```    Soldiers: " + str(offers[i][2]) + "```"
                        txt += "```    Rebirths: " + str(offers[i][3]) + "```"
                        txt += "```  ALL FOR " + str(offers[i][4]) + " GEMS!```"
                        if i != len(offers) - 1:
                            txt += "``` ```"
                    await message.channel.send(str(txt))
                else:
                    await message.channel.send("```There are not any offers currently!```")
            else:
                await message.channel.send("```Create an account first!```")

        if message.content.startswith(str(default_call) + "buy pack"):
            if findPlayer(str(message.author)) != 'nil':
                pinfo = players_playing[findPlayer(str(message.author))]
                entity = 13
                content = str(message.content)
                content += '|'
                output = ''
                while content[entity] != '|':
                    output += str(content[entity])
                    entity += 1
                try:
                    output = int(output)
                    output -= 1
                    if output >= 0:
                        if pinfo[13] >= offers[output][4]:
                            players_playing[findPlayer(str(message.author))][5] += offers[output][0]
                            players_playing[findPlayer(str(message.author))][7][0] += offers[output][1]
                            players_playing[findPlayer(str(message.author))][4] += offers[output][2]
                            players_playing[findPlayer(str(message.author))][9] += offers[output][3]
                            players_playing[findPlayer(str(message.author))][13] -= offers[output][4]
                            await message.channel.send("```You bought Pack " + str(output + 1) + " for " + str(offers[output][4]) + " gems!```")
                        else:
                            await message.channel.send("```You do not have enough gems!```")
                    else:
                        await message.channel.send("```Please select a valid pack!```")
                except ValueError:
                    await message.channel.send("```Please state a number!```")
                except IndexError:
                    await message.channel.send("```Please select a valid pack!```")
            else:
                await message.channel.send("```Create an account first!```")

        if message.content.lower() == str(default_call) + "sell all books":
            if findPlayer(str(message.author)) != 'nil':
                pinfo = players_playing[findPlayer(str(message.author))]
                if len(pinfo[10]) != 0:
                    num = len(pinfo[10]) * 1000
                    players_playing[findPlayer(str(message.author))][5] += num
                    players_playing[findPlayer(str(message.author))][10] = []
                    await message.channel.send("```You sold all your books for $" + str(num) + "!```")
                else:
                    await message.channel.send("```You don't have any books!```")
            else:
                await message.channel.send("```Create an account first!```")

        if message.content.startswith(str(default_call) + "guild "):
            if message.content.startswith(str(default_call) + "guild create "):
                if findPlayer(str(message.author)) != 'nil':
                    entity = 17
                    content = str(message.content)
                    content += '|'
                    output = ''
                    while content[entity] != '|':
                        output += str(content[entity])
                        entity += 1
                    if guildFind(output) == 'nil':
                        if not inGuild(str(message.author)):
                            if len(output) > 3:
                                guilds.append([[output], str(message.author)])
                                players_playing[findPlayer(str(message.author))][14] = output
                                await message.channel.send("```You created a guild called '" + str(output) + "'!```")
                            else:
                                await message.channel.send("```Guild name has to be at least 3 characters long```")
                        else:
                            await message.channel.send("```You cannot create a guild while in a guild!```")
                    else:
                        await message.channel.send("```That guild already exists!```")
                else:
                    await message.channel.send("```Create an account first!```")

            if message.content.startswith(str(default_call) + "guild join "):
                if findPlayer(str(message.author)) != 'nil':
                    entity = 15
                    content = str(message.content)
                    content += '|'
                    output = ''
                    while content[entity] != '|':
                        output += str(content[entity])
                        entity += 1
                    if guildFind(str(output)) != 'nil':
                        if not inGuild(str(message.author)):
                            if not len(guilds[guildFind(str(output))]) > 10:
                                guilds[guildFind(str(output))].append(str(message.author))
                                players_playing[findPlayer(str(message.author))][14] = output
                                await message.channel.send("```You joined the guild!```")
                            else:
                                await message.channel.send("```The guild is full!```")
                        else:
                            await message.channel.send("```You cannot join a guild while in a guild!```")
                    else:
                        await message.channel.send("```That guild does not exist!```")
                else:
                    await message.channel.send("```Create an account first!```")

            if message.content.lower() == str(default_call) + "guild leave":
                if findPlayer(str(message.author)) != 'nil':
                    if inGuild(str(message.author)):
                        pinfo = players_playing[findPlayer(str(message.author))]
                        gpop = guilds[guildFind(pinfo[14])]
                        for i in range(len(gpop)):
                            if i != 0:
                                if gpop[i] == str(message.author):
                                    guilds[guildFind(pinfo[14])].pop(i)
                                    if len(guilds[guildFind(pinfo[14])]) <= 1:
                                        guilds.pop(guildFind(pinfo[14]))
                                    players_playing[findPlayer(str(message.author))][14] = ''
                                    await message.channel.send("```You left the guild!```")
                                    return
                    else:
                        await message.channel.send("```You are not in a guild!```")
                else:
                    await message.channel.send("```Create an account first!```")

            if message.content.lower() == str(default_call) + "guild me":
                if findPlayer(str(message.author)) != 'nil':
                    pinfo = players_playing[findPlayer(str(message.author))]
                    txt = '```Your Guild: ```'
                    for i in range(len(guilds[guildFind(pinfo[14])])):
                        try:
                            txt += '```  Member #' + str(i + 1) + ": " + str(guilds[guildFind(pinfo[14])][i + 1] + "```")
                        except IndexError:
                            pass
                    await message.channel.send(txt)
                else:
                    await message.channel.send("```Create an account first!```")

        if message.content.startswith(str(default_call) + "dungeon "):
            if message.content.startswith((default_call) + "dungeon create "):
                if findPlayer(str(message.author)) != 'nil':
                    if dungeonFind(str(message.author)) == 'nil':
                        if players_playing[findPlayer(str(message.author))][4] > 100:
                            if time.time() - players_playing[findPlayer(str(message.author))][1][1] > 3600:
                                entity = 19
                                content = str(message.content)
                                content += '|'
                                output = ''
                                while content[entity] != '|':
                                    output += str(content[entity])
                                    entity += 1
                                try:
                                    output = int(output)
                                    players_playing[findPlayer(str(message.author))][1][1] = time.time()
                                    dungeons.append([output, str(message.author)])
                                    await message.channel.send("```You created your floor " + str(output) + " dungeon!```")
                                except ValueError:
                                    await message.channel.send("```Please state a valid number!```")
                            else:
                                await message.channel.send("```You can only create a dungeon every hour!```")
                        else:
                            await message.channel.send("```You need at least 1000 soldiers to create a dungeon!```")
                    else:
                        await message.channel.send("```You already created a dungeon!```")
                else:
                    await message.channel.send("```Create an account first!```")

            if message.content.startswith(str(default_call) + "dungeon join "):
                if findPlayer(str(message.author)) != 'nil':
                    if dungeonFind(str(message.author)) == 'nil':
                        entity = 17
                        content = str(message.content)
                        content += '|'
                        output = ''
                        while content[entity] != '|':
                            output += str(content[entity])
                            entity += 1
                        if dungeonFind(str(output)) != 'nil':
                            dungeons[dungeonFind(str(output))].append(str(message.author))
                            await message.channel.send("```You joined " + str(output) + "'s dungeon!```")
                        else:
                            await message.channel.send("```That person did not create a dungeon!```")
                    else:
                        await message.channel.send("```You are already in a dungeon!```")
                else:
                    await message.channel.send("```Create an account first!```")

            if message.content.lower() == str(default_call) + "dungeon start":
                if findPlayer(str(message.author)) != 'nil':
                    if dungeonFind(str(message.author)) != 'nil':
                        if dungeons[dungeonFind(str(message.author))][1] == str(message.author):
                            await message.channel.send("```Started your dungeon! You are currently killing all the monsters...```")
                            dpass = dungeons[dungeonFind(str(message.author))]
                            dlvl = dpass[0]
                            dungeons.pop(dungeonFind(str(message.author)))
                            dpass.pop(0)
                            num = 0
                            for i in range(len(dpass)):
                                pinfo = players_playing[findPlayer(dpass[i])]
                                num += round(pinfo[3] * pinfo[4] * pinfo[11] * pinfo[9])
                            if random.randint(1, 10) != 1:
                                dungeon_power = (2 ** dlvl) * 1000 * (1 + len(dpass) / 10)
                                if random.randint(int(num / 4), int(num)) >= dungeon_power:
                                    profit = [0, dlvl]
                                    for x in range(len(dpass)):
                                        players_playing[findPlayer(dpass[x])][5] += profit[0]
                                        players_playing[findPlayer(dpass[x])][7][0] += profit[1]
                                    await message.channel.send("```You cleared the dungeon! You all got $" + str(profit[0]) + " and " + str(profit[1]) + " coal!```")
                                else:
                                    for x in range(len(dpass)):
                                        players_playing[findPlayer(dpass[x])][4] = players_playing[findPlayer(dpass[x])][4] // 2
                                    await message.channel.send("```OOF! YOUR DUNGEON PARTY LOST! All of you lost 1/2 of your soldiers```")
                            else:
                                for x in range(len(dpass)):
                                    players_playing[findPlayer(dpass[x])][4] = players_playing[findPlayer(dpass[x])][4] // 2
                                await message.channel.send("```OOF! YOUR DUNGEON PARTY LOST! All of you lost 1/2 of your soldiers```")
                        else:
                            await message.channel.send("```You are not the owner of the dungeon party, thus you cannot start the dungeon```")

                    else:
                        await message.channel.send("```You did not create a dungeon!```")
                else:
                    await message.channel.send("```Create an account first!```")

        if message.content:
            if findPlayer(str(message.author)) != 'nil':
                pinfo = players_playing[findPlayer(str(message.author))]
                if len(pinfo) <= 14:
                    if len(pinfo) == 13:
                        players_playing[findPlayer(str(message.author))].append(0)
                    if len(pinfo) == 14:
                        players_playing[findPlayer(str(message.author))].append('')
                print("PP: " + str(players_playing))
                print("Passive: " + str(passive))
                print("Guilds: " + str(guilds))
                print("Dungeons: " + str(dungeons))
                minus = []
                for i in range(len(passive)):
                    hours = math.floor((time.time() - passive[len(passive) - i - 1][2]) / 3600)
                    if passive[len(passive) - 1 - i][1] <= hours:
                        passive.pop(len(passive) - 1 - i)
                for x in range(len(minus)):
                    print(minus)
                    passive.pop(minus[x])
                chan = str(message.channel)
                if "oof" in message.content.lower():
                    await message.channel.send("OOF!")
                try:
                    if message.content == keyword and event_on and chan == channel_event:
                        win = random.randint(10, 25)
                        event_on = False
                        players_playing[findPlayer(str(message.author))][6] += win
                        await message.channel.send("```" + str(message.author) + " won " + str(win) + " insta-cash!```")
                    if findPlayer(str(message.author)) != 'nil':
                        if players_playing[findPlayer(str(message.author))][4] == 0:
                            if players_playing[findPlayer(str(message.author))][3] > 10:
                                players_playing[findPlayer(str(message.author))][4] += 1
                                await message.channel.send("```Don't chicken out, come expose yourself to the challenging world! No more passive mode for you!```")
                            elif players_playing[findPlayer(str(message.author))][2] > 20:
                                players_playing[findPlayer(str(message.author))][4] += 1
                                await message.channel.send("```Don't chicken out, come expose yourself to the challenging world! No more passive mode for you!```")
                            elif players_playing[findPlayer(str(message.author))][5] > 50000:
                                players_playing[findPlayer(str(message.author))][4] += 1
                                await message.channel.send("```Don't chicken out, come expose yourself to the challenging world! No more passive mode for you!```")
                        else:
                            if random.randint(1, 100) == 1 and "Direct Message" not in chan and not event_on:
                                event_on = True
                                channel_event = chan
                                keyword = words[random.randint(1, (len(words) - 1))]
                                await message.channel.send("**GOD** just dropped his *wallet* into the Domination world!!! Type `" + str(keyword) + '` to claim the money!')
                        players_playing[findPlayer(str(message.author))][8] = round(10 * players_playing[findPlayer(str(message.author))][8]) / 10
                        players_playing[findPlayer(str(message.author))][5] = round(players_playing[findPlayer(str(message.author))][5])
                except:
                    pass
    else:
        return


client.run(token)
