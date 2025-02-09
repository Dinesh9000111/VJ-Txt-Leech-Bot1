import os
import re
import m3u8
import requests
import time
import subprocess
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)


# 📌 M3U8 वीडियो डाउनलोड और डिक्रिप्ट करने का फ़ंक्शन
async def handle_m3u8(file_name, file_url, encryption_key, m: Message):
    try:
        await m.reply_text(f"⏳ {file_name} डाउनलोड और डिक्रिप्ट हो रहा है...")

        playlist = m3u8.load(file_url)
        video_iv = playlist.keys[0].iv.replace("0x", "") if playlist.keys and playlist.keys[0] and playlist.keys[0].iv else "00000000000000000000000000000000"

        os.makedirs("video_segments", exist_ok=True)
        segment_files = []

        for i, segment in enumerate(playlist.segments):
            ts_url = os.path.join(os.path.dirname(file_url), segment.uri)
            encrypted_file = f"video_segments/encrypted_{i}.ts"
            decrypted_file = f"video_segments/decrypted_{i}.ts"

            response = requests.get(ts_url)
            with open(encrypted_file, "wb") as f:
                f.write(response.content)

            subprocess.run([
                "openssl", "enc", "-aes-128-cbc", "-d", "-nosalt",
                "-in", encrypted_file,
                "-K", encryption_key,
                "-iv", video_iv,
                "-out", decrypted_file
            ])

            segment_files.append(decrypted_file)
            os.remove(encrypted_file)

        output_file = f"{file_name}.mp4"
        subprocess.run([
            "ffmpeg", "-i", "concat:" + "|".join(segment_files), "-c", "copy", output_file
        ])

        for file in segment_files:
            os.remove(file)

        await upload_to_telegram(m, output_file, file_name)
        os.remove(output_file)

    except Exception as e:
        await m.reply_text(f"❌ एरर: {str(e)}")


# 📌 URL प्रोसेस करने वाला फ़ंक्शन
async def process_url(url, name, m: Message):
    if 'videos.classplusapp' in url:
        url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}',
                           headers={'x-access-token': 'your_token'}).json()['url']

    elif "utkarshapp.mpd" in url:
        id = url.split("/")[-2]
        url = f"https://apps-s3-prod.utkarshapp.com/{id}/utkarshapp.com"

    elif 'madxapi' in url:
        id = url.split("/")[-2]
        url = f"https://madxapi-d0cbf6ac738c.herokuapp.com/{id}/master.m3u8?token=your_token"

    elif "brightcove" in url:
        id = url.split("/")[-2]
        url = f"https://edge.api.brightcove.com/playback/v1/accounts/videos/{id}/master.m3u8?token=your_token"

    if ".m3u8" in url:
        encryption_key = "your_encryption_key"
        await handle_m3u8(name, url, encryption_key, m)
        return

    cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
    await m.reply_text(f"🚧 डाउनलोडिंग शुरू: {name}...")
    
    try:
        os.system(cmd)
        await upload_to_telegram(m, f"{name}.mp4", name)
        os.remove(f"{name}.mp4")
    except Exception as e:
        await m.reply_text(f"❌ डाउनलोड एरर: {str(e)}")


# 📌 टेलीग्राम पर अपलोड करने का फ़ंक्शन
async def upload_to_telegram(m: Message, file_path: str, file_name: str):
    try:
        caption = f"📄 **Title:** {file_name}\n📥 **Downloaded by:** @ilapss"
        await m.reply_text(f"📤 अपलोड हो रहा है: {file_name}...")

        if file_path.endswith(".mp4"):
            await bot.send_video(m.chat.id, video=file_path, caption=caption)
        elif file_path.endswith(".pdf"):
            await bot.send_document(m.chat.id, document=file_path, caption=caption)
        elif file_path.endswith(".gif"):
            await bot.send_animation(m.chat.id, animation=file_path, caption=caption)
        
        await m.reply_text(f"✅ {file_name} अपलोड हो गया!")
    except FloodWait as e:
        await m.reply_text(f"⚠️ टेलीग्राम लिमिट: {e.x} सेकंड तक रुको...")
        time.sleep(e.x)
        await upload_to_telegram(m, file_path, file_name)
    except Exception as e:
        await m.reply_text(f"❌ अपलोड एरर: {str(e)}")


# 📌 डाउनलोडिंग हैंडलर
@bot.on_message(filters.command("download"))
async def download_handler(client, m: Message):
    msg_parts = m.text.split(" ", 1)
    if len(msg_parts) < 2:
        await m.reply_text("⚠️ कृपया एक वैध URL दें!")
        return

    url = msg_parts[1]
    name = f"video_{int(time.time())}"

    await process_url(url, name, m)


# 📌 स्टार्ट कमांड
@bot.on_message(filters.command("start"))
async def start_handler(client, m: Message):
    await m.reply_text("👋 नमस्ते! यह बॉट M3U8, MP4, और PDF फाइल्स डाउनलोड करके टेलीग्राम पर भेज सकता है।\n\n🔹 वीडियो डाउनलोड करने के लिए /download <URL> भेजें।")


# 📌 बॉट रन करें
bot.run()
