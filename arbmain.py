import discord
import random
from discord.ext import commands

intents = discord.Intents.all()
intents.typing = False

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot已經登入：{bot.user.name}')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1119576592881037342)
    await channel.send(f'{member} 歡迎加入☆')
#成員加入訊息

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1119576592881037342)
    await channel.send(f'{member} 姊姊下次再來~☆')
#成員退出訊息

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')
#回傳機器人延遲

@bot.command()
async def 運勢(ctx):    
    random_pic = random.choice(["☆大吉☆","☆中吉☆","☆吉☆","☆兇☆"])
    await ctx.send(random_pic)
#算命

@bot.command()
async def 行不行(ctx):    
    random_num = random.randint(1,100)
    random_pic2 = random.choice(["行","不行"])
    message_content = str(random_num) + "%" + str(random_pic2)
    await ctx.send(message_content)
#行不行

@bot.command()
async def 單抽(ctx):
    def random_character():
        characters = ['☆SSR☆', '☆SR☆', '☆R☆']
        weights = [0.03, 0.17, 0.8]
        character = random.choices(characters, weights=weights, k=1)[0]
        return character   
    
    characters = [random_character() for _ in range(1)]
    result = ' '.join(characters)
    await ctx.send(result)
#單抽

@bot.command()
async def 十連(ctx):
    def random_character():
        characters = ['☆SSR☆', '☆SR☆', '☆R☆']
        weights = [0.03, 0.17, 0.8]
        character = random.choices(characters, weights=weights, k=1)[0]
        return character   
    
    characters = [random_character() for _ in range(10)]
    result = ' '.join(characters)
    await ctx.send(result)
#十連

@bot.command()
async def 給你棒棒糖(ctx):    
    random_pic = random.choice(["啊?","姊姊是想收買我嗎","你為什麼會有這個!?"])
    await ctx.send(random_pic)


@bot.event
async def on_message(message):
    if not message.author.bot:  # 忽略機器人自己發送的訊息
        content = message.content
        if content.startswith('隱藏'):  # 替換 '前綴詞' 為你想要的前綴詞
            new_content = content[len('前綴詞'):]  # 去除前綴詞
            await message.delete()  # 刪除用戶的原始訊息
            await message.channel.send(new_content)  # 由機器人發送修改後的訊息
        elif '亂數' in message.content:
            await message.channel.send('有人叫我嗎~☆')

    await bot.process_commands(message)

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 1123251123290116156:
        if str(payload.emoji) == '<:emoji_1:1123273460404191314>':
            print(f'Reaction ID for emoji_1: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123250465807810661)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')
        
        if str(payload.emoji) == '<:emoji_2:1123281745991716886>':
            print(f'Reaction ID for emoji_2: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123250392260690033)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

        if str(payload.emoji) == '<:emoji_3:1123281812576276491>':
            print(f'Reaction ID for emoji_3: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123267934370930781)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

    elif payload.message_id == 1123296427100086413:
        if str(payload.emoji) == '<:emoji_4:1123281899792633937>':
            print(f'Reaction ID for emoji_4 in message 2: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123268121793413171)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

        if str(payload.emoji) == '<:emoji_5:1123281993787002942>':
            print(f'Reaction ID for emoji_4 in message 2: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123268356481495200)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

        if str(payload.emoji) == '<:emoji_6:1123287761424764958>':
            print(f'Reaction ID for emoji_6 in message 2: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123268644999282879)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')
    
    elif payload.message_id == 1123296847151251586:
        if str(payload.emoji) == '<:emoji_7:1123287835823308870>':
            print(f'Reaction ID for emoji_7 in message 3: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123268855914037319)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

        if str(payload.emoji) == '<:emoji_8:1123287898641408061>':
            print(f'Reaction ID for emoji_8 in message 3: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123268998923042987)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

        if str(payload.emoji) == '<:emoji_9:1123287993323638925>':
            print(f'Reaction ID for emoji_9 in message 3: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123269175490654308)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

    elif payload.message_id == 1123297459695779910:
        if str(payload.emoji) == '<:emoji_10:1123288054988279978>':
            print(f'Reaction ID for emoji_10 in message 4: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123269310111039538)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

        if str(payload.emoji) == '<:emoji_11:1123288114635493377>':
            print(f'Reaction ID for emoji_11 in message 4: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123269529934495784)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

        if str(payload.emoji) == '<:emoji_12:1123288180003700887>':
            print(f'Reaction ID for emoji_12 in message 4: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123269719978422323)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

    elif payload.message_id == 1123297693050089572:
        if str(payload.emoji) == '<:emoji_13:1123288247569756260>':
            print(f'Reaction ID for emoji_13 in message 5: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123269953152364634)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

        if str(payload.emoji) == '<:emoji_14:1123288338275774506>':
            print(f'Reaction ID for emoji_14 in message 5: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123270063030542437)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

        if str(payload.emoji) == '<:emoji_15:1123288372044111902>':
            print(f'Reaction ID for emoji_15 in message 5: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123270213337632768)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

    elif payload.message_id == 1123297971556077700:
        if str(payload.emoji) == '<:emoji_16:1123288481502867586>':
            print(f'Reaction ID for emoji_16 in message 6: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123270361870499972)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

        if str(payload.emoji) == '<:emoji_17:1123288551598084207>':
            print(f'Reaction ID for emoji_17 in message 6: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123270490283327599)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

        if str(payload.emoji) == '<:emoji_18:1123288596594557050>':
            print(f'Reaction ID for emoji_18 in message 6: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123270671036846253)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

    elif payload.message_id == 1123504724960878672:
        if str(payload.emoji) == '<:emoji_19:1123503588749090836>':
            print(f'Reaction ID for emoji_19 in message 7: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123271076839968788)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

        if str(payload.emoji) == '<:emoji_20:1123503654876500038>':
            print(f'Reaction ID for emoji_20 in message 7: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123271442407112754)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

        if str(payload.emoji) == '<:emoji_21:1123503997014253619>':
            print(f'Reaction ID for emoji_21 in message 7: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123271299792375918)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

        if str(payload.emoji) == '<:emoji_22:1123504040920236032>':
            print(f'Reaction ID for emoji_22 in message 7: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123271570857664573)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')

    elif payload.message_id == 1123957255075790908:
        if str(payload.emoji) == '<:emoji_23:1123956141374849146>':
            print(f'Reaction ID for emoji_19 in message 7: {payload.emoji.id}')
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(1123957437746131076)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f'Added role {role.name} to {member.display_name}')


bot.run('MTEyMzIxMjk5NDY2NzYyMjQ4MA.GzwSc4.TiIV7E1RnfTNTdCJrd3gnV3ugxxGzISC2zRk4M')