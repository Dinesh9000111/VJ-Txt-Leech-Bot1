import os
import subprocess
import requests
import re
from pyrogram import Client, filters

# बॉट के लिए क्रेडेंशियल्स
API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

bot = Client("M3U8DownloaderBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# M3U8 डाउनलोड और प्रोसेस करने का फ़ंक्शन
def download_m3u8_video(m3u8_url, output_file="output.mp4"):
    try:
        # .m3u8 फाइल डाउनलोड करें
        m3u8_file = "video.m3u8"
        subprocess.run(["wget", "-O", m3u8_file, m3u8_url])

        # M3U8 फाइल से .ts URLs निकालें
        with open(m3u8_file, "r") as f:
            lines = f.readlines()

        ts_urls = [line.strip() for line in lines if line.strip().endswith(".ts")]
        base_url = "/".join(m3u8_url.split("/")[:-1]) + "/"

        # सभी .ts फाइलें डाउनलोड करें
        for i, ts_file in enumerate(ts_urls):
            ts_url = base_url + ts_file
            subprocess.run(["wget", "-O", f"part_{i}.ts", ts_url])

        # सभी .ts फाइलों को मर्ज करें
        with open("file_list.txt", "w") as f:
            for i in range(len(ts_urls)):
                f.write(f"file 'part_{i}.ts'\n")

        subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", "file_list.txt", "-c", "copy", output_file])

        return output_file

    except Exception as e:
        return f"Error: {str(e)}"

# टेलीग्राम कमांड हैंडलर
@bot.on_message(filters.command("download") & filters.text)
def fetch_video(client, message):
    m3u8_url = message.text.split(" ", 1)[-1]
    
    if not m3u8_url.startswith("http"):
        message.reply("कृपया एक वैध M3U8 URL दें।")
        return

    message.reply("वीडियो डाउनलोड हो रहा है, कृपया इंतजार करें...")

    output_file = download_m3u8_video(m3u8_url)

    if os.path.exists(output_file):
        message.reply_video(output_file, caption="आपका वीडियो तैयार है 🎥")
        os.remove(output_file)  # Cleanup
    else:
        message.reply("डाउनलोड या प्रोसेसिंग में समस्या आई।")

# बॉट रन करें
bot.run()
