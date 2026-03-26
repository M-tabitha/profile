import codecs
import re

html_path = r"d:\website\portfolio\index.html"
with codecs.open(html_path, "r", "utf-8") as f:
    text = f.read()

replacements = {
    "I have high level experience in web design, development knowledge and producing quality work": "I specialize in crafting compelling narratives for corporate brands and impactful promotional content for NGOs.",
    
    "I'm a web developer, with extensive knowledge and years of experience, working with quality work in web technologies, UI and UX design": "I'm a professional video editor with extensive experience in corporate storytelling, documentary-style NGO promos, and high-end post-production.",
    
    "The services we provide for design": "Corporate Brand Anthem",
    "Two smartphones displaying a sleek, dark-themed dashboard interface": "A dynamic and engaging promotional video produced for a major corporate client.",
    
    "Mobile App Lanfing Design & App Maintain": "Global Health Initiative",
    "A stylish burger restaurant mobile app interface displayed on two smartphones": "A heartwarming documentary-style campaign raising awareness for global health.",
    
    "Logo Design Creativity & Application": "Product Launch Promo",
    "Three smartphone screens displaying a beautifully designed travel booking application interface": "Fast-paced, high-energy promotional video highlighting a new tech product.",
    
    "Mobile App Landing Design & Services": "Education for All NGO",
    "Modern workout website interface design featuring a bold and energetic visual layout": "Inspiring narrative piece driving donations for international education efforts.",
    
    "Design for Technology & Services": "Internal Corporate Comms",
    "An app design that is clean, functional, and ideal for gamers looking to manage their digital assets and purchases": "Clear, professional executive messaging targeted at internal stakeholders.",
    
    "App for Technology & Services": "Wildlife Conservation Promo",
    "An app design that is clean and modern, making food browsing and ordering easy": "Visually stunning promotional cut highlighting nature conservation efforts.",
    
    "Working with Miriam was an absolute pleasure from start to finish. They took the time to truly understand our business needs and translated them into a stunning and highly functional website": "Working with Tabitha was an absolute pleasure from start to finish. She took the time to truly understand our brand guidelines and translated them into a stunning corporate anthem video.",
    
    "Miriam truly understood our business needs through her modern and sleek design, making a site incredibly user-friendly. With her help, we had a significant increase in engagement and customer sales": "Tabitha truly understood our NGO's mission. Her documentary-style editing was incredibly moving. With her help, our latest fundraising campaign saw record-breaking donations.",
    
    "I was blown away by the website Miriam created for my business! Miriam crafted a incredibly user-friendly, that allows our customers to access information on any device. Since the launch, I've seen a significant increase in inquiries and bookings": "I was blown away by the promo video Tabitha edited for our launch! She crafted an incredibly high-energy sequence that perfectly matched our vision. Engagement skyrocketed immediately."
}

for k, v in replacements.items():
    # Replace all spaces in the search string with \s+ to account for HTML line breaks and indents
    pattern = re.escape(k).replace(r'\ ', r'\s+')
    text = re.sub(pattern, v, text)

with codecs.open(html_path, "w", "utf-8") as f:
    f.write(text)

print("Regex semantic replacements complete.")
