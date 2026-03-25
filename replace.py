import codecs
import random
import re

html_path = r"d:\website\portfolio\index.html"
with codecs.open(html_path, "r", "utf-8") as f:
    text = f.read()

urls = [
    "https://i.postimg.cc/3NgvPcZD/home-img.png",
    "https://i.postimg.cc/W1YZxTpJ/about-img.jpg",
    "https://i.postimg.cc/43Th5VXJ/work-1.png",
    "https://i.postimg.cc/sXLjnC5p/work-2.png",
    "https://i.postimg.cc/QNB1jXYZ/work-3.png",
    "https://i.postimg.cc/s2DGqyG8/work-4.png",
    "https://i.postimg.cc/TYVyPhrF/work-5.png",
    "https://i.postimg.cc/wMdqKcbv/work-6.png",
    "https://i.postimg.cc/MTr9j4Yn/client1.jpg",
    "https://i.postimg.cc/wvV7f8rB/client2.jpg",
    "https://i.postimg.cc/pdP9DL0S/client3.jpg"
]

videos = [
    "uploads/SANURA/Cinnamon Final.mp4",
    "uploads/SANURA/Gold Final.mp4",
    "uploads/SANURA/Grape Final.mp4",
    "uploads/SANURA/Sunset Final.mp4",
    "uploads/SANURA/Vanilla Final.mp4"
]

# Randomly pick media for each url
for url in urls:
    if url in text:
        vid = random.choice(videos)
        # We need to find the specific img tag that has this url
        # Find exactly <img ... class="...">
        pattern = r'<img\s+src="' + re.escape(url) + r'"\s*alt="[^"]*"\s*class="([^"]+)">'
        replacement = f'<video src="{vid}" class="\\1" autoplay loop muted playsinline></video>'
        text = re.sub(pattern, replacement, text)

# Just in case some URLs matched without the exact img tag order, we can also do a backup replace
# Wait, let's just do it directly with a function that replaces any img tag that has one of these URLs

def replace_img(match):
    full_match = match.group(0)
    for url in urls:
        if url in full_match:
            vid = random.choice(videos)
            # extract class
            class_match = re.search(r'class="([^"]+)"', full_match)
            cls = class_match.group(1) if class_match else ""
            if cls:
                return f'<video src="{vid}" class="{cls}" autoplay loop muted playsinline></video>'
            else:
                return f'<video src="{vid}" autoplay loop muted playsinline></video>'
    return full_match

text = re.sub(r'<img\s+[^>]*src="https://i\.postimg\.cc/[^>]+>', replace_img, text)

with codecs.open(html_path, "w", "utf-8") as f:
    f.write(text)

print("Replacement complete.")
