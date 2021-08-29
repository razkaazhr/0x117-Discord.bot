import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = ">> ")
@client.event
async def on_member_join(member):
    print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):
    print(f"{member}has left the server.")

   
@client.event
async def on_ready():
    print("  [+] checking python code: ✔  [+]")
    print("  [+] searching for bugs in the code: ✔  [+]")
    print("  [+] feeding cats: ✔   [+]")
    print("  [+] bot is ready! [+] ")

@client.command()
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@client.command()
async def alive(ctx):
    await ctx.send(f"ngapa 🆖🆎 {round(client.latency * 1000)}ms")

@client.command()
async def sus(ctx):
    await ctx.send("https://tenor.com/view/sus-suspect-among-us-gif-18663592")

@client.command()
async def rape(ctx):
    await ctx.send("*suddenly gets kidnapped and groped for 3 hours then, reaches an unknown place then puills out the pussy raper 6000 and gets raped for 4 hours with continuous cum*")



@client.command()
async def master(ctx):
    await ctx.send("https://gfycat.com/thunderouseverlastingequestrian")


@client.command()
async def haxx(ctx):
    await ctx.send("https://discord.gg/abHWxqEmFk")


@client.command(aliases=["8ball", "test"])
async def _8ball(ctx, *, question):
    responses = ["iya.",
                "ngga.",
                "kontolah.",
                "i doont think so buddy",
                "there goes a friend",
                "setuju beut,",
                "ngoghey.",
                "💖💖💖.",
                "fuck you dumbass.",
                "ngl ur correctz😍😍",
                "NGENTOT.",
                "ANJING.",
                "gatau nih men dia agax su",
                "LANGSUNG BORRRRRRRRR!",
                "iya memang",
                "kata sapa?",
                "🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️",
                "sus",
                "A M O G U S",
                "¯\_( ͡❛ ͜ʖ ͡❛)_/¯",
                "O̲ppa̲ (っ-̶●̃益●̶̃)っ ,︵‿ S̲t̲yl̲e̲",
                "☣☣☣☣",
                "SUS",]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@client.command(aliases=["bully", "b"])
async def _8bully(ctx, *, crasont):
    responses = ["emang anak kontol dia",
    "ga nyadar dia, diakan anak haram botis hasil kondom bocor",
    "bapak nya pas dia lahir pergi buat beli pemper tp ga balik2 lagi HAHA canda anak kondom bocor",
    "ke pasar beli opor, kalo kamu pelakor ahay canda pelakor",
    "thats why yo momma dead lol",
    "lol titid kecil",
    "sticks and stones dont break my heart, but dildos and cocks break yo mommas heat",]
    await ctx.send(f"who we bullyin: {crasont}\nbully: {random.choice(responses)}")


@client.command(name='spam', help='it spams you daft cunt')
async def spam(ctx, amount:int, *, message):
    for i in range(amount): 
        await ctx.send(message)



@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")


@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)


@client.command()

async def kick(ctx, member: discord.Member, *, reason=None):

    await member.kick(reason=reason)

    await ctx.send(f'User {member} has kicked.')


@commands.command()
@commands.has_permissions(ban_members=True)
async def ban(self, ctx, member: discord.Member, *, reason=None):
     await member.ban(reason=reason)
     await ctx.send(f'User {member} has been kick')





@client.command(name="join")
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command(name="leave")
async def leave(ctx):
    channel = ctx.author.voice.channel
    await channel.disconnect()
    print('bye dumb bitch')

@client.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@client.group()
async def hack(ctx):
    """hacks a user (NOT REAL)
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('hacking {0.subcommand_passed} https://c.tenor.com/YbmQHDSJvbkAAAAS/thumbs-up-hacker.gif https://c.tenor.com/Ry-jYCyu2O8AAAAM/mega64-hacking-in-progress.gif https://c.tenor.com/9ItR8nSuxE0AAAAM/thumbs-up-computer.gif {0.subcommand_passed} has been hacked!'.format(ctx))


@client.group()
async def Rape(ctx):
    """rapes a user
    lmao
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(' {0.subcommand_passed} was kidnappped and whilst he was at the back of the white truck geeting groped for 3 hours the driver drove 5 km and when they reached the destination, {0.subcommand_passed} was raped by the rape inator made by heinz doofensmirtz for 3 hours'.format(ctx))

@client.group()
async def dab(ctx):
    """piss on a user.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('''AY YO {0.subcommand_passed} DAB ME UP?
       https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFIY6rtXFC8KBQb5zodyTxUXVLvclEs62EhHlGxsI-xU1OJAQhxrEZc0ha4zXkpp7tmb0&usqp=CAU '''.format(ctx))



@client.group()
async def piss(ctx):
    """piss on a user.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('fuck you dumbass, {0.subcommand_passed} i hope you get ru by a car and get raped by a fucking dog and when you die nobody will come to your funeral because you dont have any fucking friends and you dont have a fucking life so get out and get a fucking life you faggot'.format(ctx))

@client.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@client.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@client.command()
async def invite(ctx):
    '''Invite the bot to your server'''
    await ctx.send(
        f"Invite me to your server : put discord bot invite url here")


client.run('put your discord bot token here')

