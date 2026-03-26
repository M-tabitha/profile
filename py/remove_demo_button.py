import codecs
import re

html_path = r"d:\website\portfolio\index.html"
with codecs.open(html_path, "r", "utf-8") as f:
    text = f.read()

# 1. Remove the demo span
pattern = re.compile(r'<span\s+class="work-button"\s*>\s*Demo\s*<i\s+class="uil\s+uil-arrow-right\s+work-button-icon"\s*>\s*</i>\s*</span>', re.IGNORECASE)
text = pattern.sub('', text)

# 2. Add work-button class to work-img video elements
text = text.replace('class="work-img"', 'class="work-img work-button" style="cursor: pointer;"')

with codecs.open(html_path, "w", "utf-8") as f:
    f.write(text)

print("Demo buttons removed, video previews set as buttons.")
