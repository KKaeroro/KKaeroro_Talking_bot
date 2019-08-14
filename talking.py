import discord
import os
import asyncio
import re
import random
import urllib
import urllib.request
import os
import sys
import json
import time
import datetime


client = discord.Client()


@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
    print(f'Ready')
    await client.change_presence(game=discord.Game(name="(로로야 (질문) 으로 나눠보세요.)", type=1))

@client.event
async def on_message(message):
    if message.content.startswith('로로야 안녕') or message.content.startswith('로로야 ㅎㅇ') or message.content.startswith('로로야 안룡') or message.content.startswith('로로야 Hi') or message.content.startswith('로로야 안냐') or message.content.startswith('로로야 안녕하세요') or message.content.startswith('로로야 안녕하십니까') or message.content.startswith('로로야 하위') or message.content.startswith('로로야 ㅎ2') or message.content.startswith('로로야 하2') or message.content.startswith('로로야 하이') or message.content.startswith('로로야 안뇽'):
        randomNum = random.randrange(1, 15)
        if randomNum==1:
            await client.send_message(message.channel, "너한테 안녕 받을 기분 아니다.")
        if randomNum==2:
            await client.send_message(message.channel, "https://i.pinimg.com/originals/cf/0a/f0/cf0af085489716864b4d1fea938d0e5b.jpg")
        if randomNum==3:
            await client.send_message(message.channel, "https://i.pinimg.com/originals/52/4d/4e/524d4e99191388d3deb8bc45d4b1d69a.jpg")
        if randomNum==4:
            await client.send_message(message.channel, "http://gangple.com/data/file/story/990506455_anxfGBVy_491f27e571d80eace2043fa70ba24a03dd48fecd.jpeg")
        if randomNum==5:
            await client.send_message(message.channel, "그냥 거울 보고 인사 하는 것 밖에 더 되냐? ㅋㅋㅋ")
        if randomNum==6:
            await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/606188013885718532/610073267587383329/Z.png")
        if randomNum==7:
            await client.send_message(message.channel, "이봐, 자네 인사하고 가는 김에 똥 좀 가지고 가!")
        if randomNum==8:
            await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/606188013885718532/609402235381612565/1466248815399_1440083797.png")
        if randomNum==9:
            await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/606188013885718532/609401766026412061/53000058_412351119540268_3949938788373402741_n.png")
        if randomNum==10:
            await client.send_message(message.channel, "얼굴도 못생긴게 자꾸 나불 거려. 나는 얼굴 못생긴 애 하고는 안 놀아")
        if randomNum==11:
            await client.send_message(message.channel, "미안한데 역겨운 냄새가 나서 인사 안 받아줄게.")
        if randomNum==12:
            await client.send_message(message.channel, "https://previews.123rf.com/images/mackdsgn/mackdsgn1608/mackdsgn160800049/62063121-%EA%B2%BD%EA%B3%A0-%EC%95%84%EC%9D%B4%EC%BD%98%EC%9E%85%EB%8B%88%EB%8B%A4-%EC%9C%84%ED%97%98-%EC%95%84%EC%9D%B4%EC%BD%98%EC%9E%85%EB%8B%88%EB%8B%A4-%EC%A3%BC%EC%9D%98-%EC%95%84%EC%9D%B4%EC%BD%98.jpg \n 아이고 오류가 나버렸네?")
        if randomNum==13:
            await client.send_message(message.channel, "똥 만진 손으로 어디서 인사질이야! 저리 꺼져줄래.")
        if randomNum==14:
            await client.send_message(message.channel, "ㅇㅇ")
        if randomNum==15:
            await client.send_message(message.channel, "안녕이라고 말하지마 - 다비치 https://www.youtube.com/watch?v=SGmnGLN-6YU")
            
    if message.content.startswith('로로야 뭐하니') or message.content.startswith('로로야 뭐함') or message.content.startswith('로로야 뭐하누') or message.content.startswith('로로야 ㅁㅎ') or message.content.startswith('로로야 뭐하고있어') or message.content.startswith('로로야 무함') or message.content.startswith('로로야 머해') or message.content.startswith('로로야 뭐해') or message.content.startswith('로로야 머함') or message.content.startswith('로로야 머하고 있어'):
        randomNum = random.randrange(1, 15)
        if randomNum==1:
            await client.send_message(message.channel, "니 얼굴 보고 화장실 좀 다녀왔어")
        if randomNum==2:
            await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/606188013885718532/609402376620736512/90d6c1fe3001fd71370071c6b392c2af.png")
        if randomNum==3:
            await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/606188013885718532/609400250012139565/A4fwo0HCAAAgSyj.png")
        if randomNum==4:
            await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/606188013885718532/609301698137030666/FB_IMG_1563236769991.jpg")
        if randomNum==5:
            await client.send_message(message.channel, "뭐하기 뭐해 니 얼굴 조질 생각 하고 있지")
        if randomNum==6:
            await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/606188013885718532/609301695360663558/FB_IMG_1563236776623.jpg")
        if randomNum==7:
            await client.send_message(message.channel, "너의 얼굴을 보고 토 했던 거를 보고 있었어")
        if randomNum==8:
            await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/606188013885718532/609402235381612565/1466248815399_1440083797.png")
        if randomNum==9:
            await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/606188013885718532/609401766026412061/53000058_412351119540268_3949938788373402741_n.png")
        if randomNum==10:
            await client.send_message(message.channel, "얼굴도 못생긴게 자꾸 나불 거려. 나는 얼굴 못생긴 애 하고는 안 놀아")
        if randomNum==11:
            await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/606188013885718532/609401546819502080/2741954D5433D4B00D79BB.png")
        if randomNum==12:
            await client.send_message(message.channel, "https://previews.123rf.com/images/mackdsgn/mackdsgn1608/mackdsgn160800049/62063121-%EA%B2%BD%EA%B3%A0-%EC%95%84%EC%9D%B4%EC%BD%98%EC%9E%85%EB%8B%88%EB%8B%A4-%EC%9C%84%ED%97%98-%EC%95%84%EC%9D%B4%EC%BD%98%EC%9E%85%EB%8B%88%EB%8B%A4-%EC%A3%BC%EC%9D%98-%EC%95%84%EC%9D%B4%EC%BD%98.jpg \n 아이고 오류가 나버렸네?")
        if randomNum==13:
            await client.send_message(message.channel, "미안한데 손절 할게 빠이!\nhttps://cdn.discordapp.com/attachments/606188013885718532/610398171910111232/FB_IMG_1563236704090.jpg")
        if randomNum==14:
            await client.send_message(message.channel, "차단할게요.")
        if randomNum==15:
            await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/606188013885718532/609402045434167306/66034756_2840223759326983_7170769609649667124_n.png")

client.run('NjExMDc0MTE0MTU2NzU3MDEz.XVOhKw.7diTmtA9CkrtYecqeHx_u9vLaCI')
            