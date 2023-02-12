import mysql.connector as connector
import discord
from discord.ext import commands
connect=connector.connect(
    host="host",
    user="user name",
    password="password of user",
    database="db name"
    
)

cursor=connect.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS role (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), role VARCHAR(255))")

intents = discord.Intents.default()
intents.message_content = True
intents.members= True
# intents.guilds=True
intents.messages=True

#client(bot) command
client=commands.Bot(command_prefix='--',intents=intents)

@client.command(name='exodus')
async def exodus(context):
    await context.message.channel.send('Hello I am exodus')
  
    
    
#Bot online message

@client.event
async def on_ready():
    #functions
    general_channel= client.get_channel(channel id)

    await general_channel.send("Hello I'm online")
    
@client.event
#bot welcome message    
@client.event
async def on_member_join(member):
    guild=member.guild
    message = f"Welcome to the {guild.name} server, {member.mention}! Please take a moment to read the rules and introductions in the appropriate channels."
    channel = discord.utils.get(guild.channels, name="welcome")
    await channel.send(message)
    
#bot answer to question
    
@client.event
async def on_message(message):
    if message.content == 'what are you':
        general_channel= client.get_channel(1073610527533699123)
        
        myEmbed = discord.Embed(title="What am I?",description="Bot by Exodus",color=0x183515)
        myEmbed.add_field(name="Owner",value="Exodus",inline=False)
        myEmbed.set_author(name="Exo_bot")
        await general_channel.send(embed=myEmbed)
    await client.process_commands(message)
#reaction by bot    
@client.event
async def on_reaction_add(reaction, user):
    # I do not actually recommend doing this.
    author=reaction.message.author
    async for user in reaction.users():
        await reaction.message.channel.send(f'{user} has reacted with {reaction.emoji}! to {author.name} ')

#parameterised command
@client.command(name='role')
async def create_roles(ctx,name):
    existing_role = discord.utils.get(ctx.guild.roles, name=name)
    if existing_role:
            await ctx.channel.send(f"Role '{name}' already exists.")
            return
    new_role = await ctx.guild.create_role(name=name)
    await ctx.author.add_roles(new_role)
    await ctx.channel.send(f"Role '{name}' created and added to {ctx.author.mention}.")
    
    
    
    
    connect.commit()
    
@client.command(name='add')
async def add_user(ctx,name):
    cursor.execute(f"select * from role where role=  '{name}'")
    result=cursor.fetchall()
    if result:
        await ctx.channel.send("Already entered")
        return
    cursor.execute(f"insert into role (role) values ('{name}')")
    connect.commit()




#run client in server
client.run('your discord token')
