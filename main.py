# Don't Remove Credit Tg - @SONICKUWALSSCBOT
# website 🚩 For Amazing Bot https://sonickuwalssc.blogspot.com/
# Ask Doubt on telegram @SONICKUWALUPDATEKANHA

import os
import re
import sys
import json
import time
import aiohttp
import asyncio
import requests
import subprocess
import urllib.parse
import yt_dlp
import cloudscraper
import datetime
import ffmpeg
import logging 

from yt_dlp import YoutubeDL
import yt_dlp as youtube_dl
from pytube import YouTube
from aiohttp import web

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)



@bot.on_message(filters.command(["start"]))
async def start(bot: Client, m: Message):
    editable = await m.reply_text(
       f" You are currently using the free version. 🆓\n\n"
    "I'm here to make your life easier by downloading videos from your **.txt** file 📄 and uploading them directly to Telegram!\n\n"
    "Want to get started? \n\n💬 Contact @ilaps to Get The Subscription 🎫 and unlock the full potential of your new bot! 🔓")
    
@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**Stopped**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


@bot.on_message(filters.command(["moon"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('𝕤ᴇɴᴅ ᴛxᴛ ғɪʟᴇ  **')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)
    
    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))
        os.remove(x)
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    
   
    await editable.edit(f"**𝕋ᴏᴛᴀʟ ʟɪɴᴋ𝕤 ғᴏᴜɴᴅ ᴀʀᴇ🔗🔗** **{len(links)}**\n\n**𝕊ᴇɴᴅ 𝔽ʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪ𝕤** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Now Please Send Me Your Batch Name**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)

    await editable.edit("**𝔼ɴᴛᴇʀ ʀᴇ𝕤ᴏʟᴜᴛɪᴏɴ📸**\n144,240,360,480,720,1080 please choose quality")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    

    await editable.edit("Now Enter A Caption to add caption on your uploaded file")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == 'Robin':
        MR = highlighter 
    else:
        MR = raw_text3
   
    await editable.edit("Now send the Thumb url/nEg »  \n Or if don't want thumbnail send = no")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            
             V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","")  .replace("mpd","m3u8")
             url = "https://" + V
             if "visionias" in url:
                 async with ClientSession() as session:
                     async with session.get(url, headers={
                     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
                     'Accept-Language': 'en-US,en;q=0.9',
                     'Cache-Control': 'no-cache',
                     'Connection': 'keep-alive',
                     'Pragma': 'no-cache',
                     'Referer': 'http://www.visionias.in/',
                     'Sec-Fetch-Dest': 'iframe',
                     'Sec-Fetch-Mode': 'navigate',
                     'Sec-Fetch-Site': 'cross-site',
                     'Upgrade-Insecure-Requests': '1',
                     'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                     'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                     'sec-ch-ua-mobile': '?1',
                     'sec-ch-ua-platform': '"Android"',}) as resp:
                         text = await resp.text()
                         url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)
                      
             elif 'videos.classplusapp' in url:
                 url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': token, }).json()['url']
              
             elif 'tencdn' in url:
                 url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': token, }).json()['url']
              
             elif 'tencdn' in url:
                 id =  url.split("/")[-2]
                 url =  "https://extractapi.vercel.app/classplus?link=https://tencdn.classplusapp.com/" + id + "/master.m3u8"
              
             elif "brightcove" in url:
                 Master = url.split("?")
                 src_url = Master[0].replace("/master.m3u8", "")
                 src_auth = Master[1].split("=")[1]
                 url = await master.generate_master_url(src_url, src_auth)
              
             elif 'testbook' in url:
                 id =  url.split("/")[-2]
                 url =  "https://extractapi.vercel.app/classplus?link=https://cpvod.testbook.com/" + id + "/playlist.m3u8"

             elif 'cpvod.testbook' in url:
                 id =  url.split("/")[-2]
                 url =  "https://extractapi.vercel.app/classplus?link=https://cpvod.testbook.com/" + id + "/playlist.m3u8"   
                           
             elif '/master.mpd' in url:
                 id =  url.split("/")[-2]
                 url =  "https://pedablu.jarviss.workers.dev?v=https://d1d34p8vz63oiq.cloudfront.net/" + id + "/master.m3u8"
            
             elif '/master.mpd' in url:
                 id =  url.split("/")[-2]
                 url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"
          
             name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
             name = f'{str(count).zfill(3)}) {name1[:60]}'

          
             if "youtu" in url:
                 ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
             else:
                 ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

             if "acecwply" in url:
                 cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
        
             elif "jw-prod" in url:
                 cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
             else:
                 cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'
   
             if "embed" in url:
                 ytf = f"bestvideo[height<={raw_text2}]+bestaudio/best[height<={raw_text2}]"
             elif "youtube" in url:
                 ytf = f"bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]/best[height<={raw_text2}][ext=mp4]"
             else:
                 ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba" 
             if "embed" in url:
                 ytf = f"bestvideo[height<={raw_text2}]+bestaudio/best[height<={raw_text2}]"
             elif "youtube" in url:
                 ytf = f"bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]/best[height<={raw_text2}][ext=mp4]"
             else:
                 ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
             if "player.vimeo" in url:
                 cmd = f'yt-dlp -f "{ytf}+bestaudio" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
         
             elif url.startswith("https://apni-kaksha.vercel.app"):
                 cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
         
             elif "m3u8" or "livestream" in url:
                 cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
         
             elif ytf == "0" or "unknown" in out:
                 cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
         
             elif ".pdf" or "download" in str(url):
                 cmd = "pdf"
             else:
                 cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
             try:         
                
                cc = f'**[🎥] VIDEO ID: {str(count).zfill(3)}**\n\n**📄 Title** : {name1}\n\n**🔖 Batch** : {raw_text0}\n\n**📥 Downloaded by : @ilapss **'
                cc1 = f'**[📁] File_ID: {str(count).zfill(3)}**\n\n**📄 Title** : {name1}\n\n**🔖 Batch** : {raw_text0}\n\n**📥 Downloaded by : @ilapss **'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o " @ilapss {name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f' @ilapss {name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f' @ilapss {name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**🚧 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐈𝐍𝐆 🚧**\n\n**🎬Name »** `{name}\n\n❄Quality » {raw_text2}`\n\n**🔗URL »** `{url}`"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading Interupted **\n{str(e)}\n**Name** » {name}\n**Link** » `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**𝔻ᴏɴᴇ 𝔹ᴏ𝕤𝕤😎**")


bot.run()
