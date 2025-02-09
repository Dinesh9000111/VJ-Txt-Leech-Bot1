import os
import random
import string
import m3u8
from datetime import datetime

# 🎯 .txt फ़ाइल से इनपुट लेने का फ़ंक्शन
def read_input_from_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.read().strip().split("\n")
            video_link = lines[0]
            audio_link = lines[1] if len(lines) > 1 else None
            encryption_key = lines[2] if len(lines) > 2 else None
            return video_link, audio_link, encryption_key
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None, None, None

# 🎯 यूज़र से इनपुट लें (या .txt फ़ाइल से)
file_input = input("📄 Enter .txt file path (or press Enter to enter manually): ").strip()
if file_input:
    video_link, audio_link, encryption_key = read_input_from_file(file_input)
else:
    video_link = input("🎥 Enter M3U8 video link: ").strip()
    audio_link = input("🎵 Enter M3U8 audio link (if available): ").strip()
    encryption_key = input("🔑 Enter the decryption key: ").strip()

current_time = datetime.now().strftime("%H%M%S")
video_iv = ""

# 📌 M3U8 से TS फाइलें डाउनलोड करने का फ़ंक्शन
def download_ts_files(link, is_audio):
    global video_iv
    playlist = m3u8.load(link)
    ts_len = len(playlist.segments)
    
    root_video_link = "/".join(link.split("/")[:-1])+"/"
    ts_filename = f"{current_time}.ts" if not is_audio else f"{current_time}_audio.ts"
    
    for i in range(ts_len):
        segment_info = str(playlist.segments[i]).split(",")
        video_iv = segment_info[2].replace("IV=0x", "").split("\n")[0]
        ts_file = segment_info[3].replace("\n", "")

        os.system(f"wget {root_video_link}{ts_file} -O ->> {ts_filename}")

# 📌 TS फाइल डिक्रिप्ट करने का फ़ंक्शन
def decrypt_ts(filename, is_audio):
    decrypted_filename = "decrypted.mkv" if not is_audio else "decrypted.aac"
    os.system(f"openssl enc -aes-128-cbc -nosalt -d -in {filename}.ts -K '{encryption_key}' -iv '{video_iv}' > {decrypted_filename}")

# 📌 वीडियो और ऑडियो को मर्ज करने का फ़ंक्शन
def merge_audio_video():
    output_filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) + ".mp4"
    os.system(f"ffmpeg -i decrypted.mkv -i decrypted.aac -c copy {output_filename}")
    
    # क्लीनअप (अनावश्यक फाइलें हटाएं)
    os.system(f"rm decrypted.mkv decrypted.aac {current_time}.ts {current_time}_audio.ts")
    print(f"✅ वीडियो सेव हो गया: {output_filename}")

# 📌 पूरा प्रोसेस रन करना
if video_link and encryption_key:
    download_ts_files(video_link, False)
    decrypt_ts(current_time, False)

if audio_link:
    download_ts_files(audio_link, True)
    decrypt_ts(current_time+"_audio", True)
    merge_audio_video()
else:
    print("🎥 Video downloaded without audio!")
