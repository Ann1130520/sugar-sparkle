import asyncio
import json
import os
import subprocess
import wave
from pathlib import Path
import edge_tts

import sys
sys.path.insert(0, r"C:\Users\User\.gemini\config\skills\motion-video\scripts")
from mvlib import CJK, GAP, LEAD_IN, TAIL, load_script, say, split_lines, ffmpeg_exe

RATE = 24000

async def generate_scene_audio(text, voice, out_mp3):
    tts = edge_tts.Communicate(text, voice, rate="+5%", pitch="+2Hz")
    await tts.save(str(out_mp3))

def convert_to_wav(in_mp3, out_wav):
    cmd = [
        ffmpeg_exe(), "-y", "-loglevel", "error",
        "-i", str(in_mp3),
        "-ar", str(RATE), "-ac", "1", "-c:a", "pcm_s16le",
        str(out_wav)
    ]
    subprocess.run(cmd, check=True)

def write_wav(path, pcm):
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(RATE)
        w.writeframes(pcm)

async def main():
    folder = Path(r"C:\Users\User\.gemini\antigravity\scratch\sugar-sparkle-website\videos\sugar_sparkle_promo")
    data = load_script(folder)
    lang = "zh"
    voice = data["voice"].get(lang, "zh-TW-HsiaoChenNeural")
    out_dir = folder / f"audio_{lang}"
    out_dir.mkdir(exist_ok=True)

    for sc in data["scenes"]:
        text = "".join(say(l) for l in sc[lang])
        print(f"Generating TTS for {sc['id']}: {text[:30]}...")
        mp3_file = out_dir / f"{sc['id']}.mp3"
        wav_file = out_dir / f"{sc['id']}.wav"
        await generate_scene_audio(text, voice, mp3_file)
        convert_to_wav(mp3_file, wav_file)
        if mp3_file.exists():
            mp3_file.unlink()

    # Build timeline and merged narration_zh.wav
    t = LEAD_IN
    tl = {"lang": lang, "lead_in": LEAD_IN, "gap": GAP, "scenes": []}
    merged = bytearray(b"\x00\x00" * int(RATE * LEAD_IN))

    for sc in data["scenes"]:
        wav_path = out_dir / f"{sc['id']}.wav"
        with wave.open(str(wav_path)) as w:
            pcm = w.readframes(w.getnframes())
        dur = len(pcm) / 2 / RATE
        tl["scenes"].append({
            "id": sc["id"],
            "start": round(t, 3),
            "dur": round(dur, 3),
            "lines": split_lines(sc[lang], lang, t, dur)
        })
        merged += pcm + b"\x00\x00" * int(RATE * GAP)
        t += dur + GAP

    tl["total"] = round(t + TAIL, 3)
    merged += b"\x00\x00" * int(RATE * TAIL)

    narration_file = folder / f"narration_{lang}.wav"
    write_wav(narration_file, bytes(merged))

    timeline_file = folder / f"timeline_{lang}.json"
    timeline_file.write_text(json.dumps(tl, ensure_ascii=False, indent=2), encoding="utf-8")

    # Update _tl.js
    from mvlib import write_tl_js
    write_tl_js(folder, data)

    print(f"[OK] Audio & Timeline complete! Total length: {tl['total']:.2f}s")
    print(f"  Narration: {narration_file}")
    print(f"  Timeline: {timeline_file}")

if __name__ == "__main__":
    asyncio.run(main())
