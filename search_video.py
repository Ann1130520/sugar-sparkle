import urllib.request
import re
import json

req = urllib.request.Request('https://www.youtube.com/results?search_query=candy+shop+commercial+aesthetic', headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    matches = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', html)
    unique = list(dict.fromkeys(matches))[:15]
    for vid in unique:
        try:
            oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
            oembed_req = urllib.request.Request(oembed_url, headers={'User-Agent': 'Mozilla/5.0'})
            res = urllib.request.urlopen(oembed_req)
            data = json.loads(res.read())
            print(f"ID: {vid} | Title: {data.get('title')}")
        except:
            pass
except Exception as e:
    print("Error:", e)
