import codecs
import re

html_path = r"d:\website\portfolio\index.html"
with codecs.open(html_path, "r", "utf-8") as f:
    text = f.read()

replacements = {
    "<title>Document</title>": "<title>Tabitha - Video Editor Portfolio</title>",
    
    "Frontend Developer": "Video Editor",
    "I have high level experience in web design, development knowledge and producing quality work": "I specialize in crafting compelling narratives for corporate brands and impactful promotional content for NGOs.",
    
    "I'm a web developer, with extensive knowledge and years of experience, working with quality work in web technologies, UI and UX design": "I'm a professional video editor with extensive experience in corporate storytelling, documentary-style NGO promos, and high-end post-production.",
    
    "BFA in Graphic Design": "BA in Film and Media",
    "Diploma in Web Design": "Corporate Comms Diploma",
    "BS in Web Development": "Advanced Video Certificate",
    "Lead / Senior UX Designer": "Senior Video Editor",
    "Web site / UX Designer": "Freelance Video Editor",
    "Junior UX Designer": "Assistant Editor",
    
    "UI / UX Design": "Motion Graphics",
    "Backend Developer": "Color Grading",
    
    '<h3 class="skills-name">HTML</h3>': '<h3 class="skills-name">Premiere Pro</h3>',
    '<h3 class="skills-name">CSS</h3>': '<h3 class="skills-name">DaVinci Resolve</h3>',
    '<h3 class="skills-name">Javascript</h3>': '<h3 class="skills-name">Final Cut Pro</h3>',
    '<h3 class="skills-name">React</h3>': '<h3 class="skills-name">Avid Media Composer</h3>',
    
    '<h3 class="skills-name">Figma</h3>': '<h3 class="skills-name">After Effects</h3>',
    '<h3 class="skills-name">Sketch</h3>': '<h3 class="skills-name">Cinema 4D</h3>',
    '<h3 class="skills-name">PhotoShop</h3>': '<h3 class="skills-name">Illustrator</h3>',

    '<h3 class="skills-name">PHP</h3>': '<h3 class="skills-name">Color Correction</h3>',
    '<h3 class="skills-name">Python</h3>': '<h3 class="skills-name">LUT Creation</h3>',
    '<h3 class="skills-name">MySQL</h3>': '<h3 class="skills-name">HDR Workflow</h3>',
    '<h3 class="skills-name">Firebase</h3>': '<h3 class="skills-name">Scopes Analysis</h3>',
    
    'data-filter=".web"': 'data-filter=".corporate"',
    'data-filter=".app"': 'data-filter=".ngo"',
    'data-filter=".design"': 'data-filter=".promo"',
    
    '>Web<': '>Corporate<',
    '>App<': '>NGO<',
    '>Design<': '>Promo<',
    
    'mix web': 'mix corporate',
    'mix app': 'mix ngo',
    'mix design': 'mix promo',
    
    'Web Design': 'Corporate Video',
    'App Design': 'NGO Campaign',
    'Brand Design': 'Promotional Content',
    
    'Role - <span>frontend</span>': 'Role - <span>Video Editor</span>',
    '<li>Technologies - <span>html css</span></li>': '<li>Technologies - <span>Premiere, After Effects</span></li>',
    
    'The services we provide for design': 'Corporate Brand Anthem',
    'Two smartphones displaying a sleek, dark-themed dashboard interface': 'A dynamic and engaging promotional video produced for a major corporate client.',
    
    'Mobile App Lanfing Design & App Maintain': 'Global Health Initiative',
    'A stylish burger restaurant mobile app interface displayed on two smartphones': 'A heartwarming documentary-style campaign raising awareness for global health.',
    
    'Logo Design Creativity & Application': 'Product Launch Promo',
    'Three smartphone screens displaying a beautifully designed travel booking application interface': 'Fast-paced, high-energy promotional video highlighting a new tech product.',
    
    'Mobile App Landing Design & Services': 'Education for All NGO',
    'Modern workout website interface design featuring a bold and energetic visual layout': 'Inspiring narrative piece driving donations for international education efforts.',
    
    'Design for Technology & Services': 'Internal Corporate Comms',
    'An app design that is clean, functional, and ideal for gamers looking to manage their digital assets and purchases': 'Clear, professional executive messaging targeted at internal stakeholders.',
    
    'App for Technology & Services': 'Wildlife Conservation Promo',
    'An app design that is clean and modern, making food browsing and ordering easy': 'Visually stunning promotional cut highlighting nature conservation efforts.',
    
    'Featured - <span>Design</span>': 'Featured - <span>Promo</span>',
    
    'Web <br> Designer': 'Corporate <br> Video',
    'Web Designer</h3': 'Corporate Video</h3',
    'UI/UX <br> Designer': 'NGO <br> Content',
    'UI/UX Designer</h3': 'NGO Content</h3',
    'Branding <br> Designer': 'Post-Prod <br> & Grading',
    'Branding Designer</h3': 'Post-Prod & Grading</h3',
    
    '<p class="services-modal-info">User Interface Development</p>': '<p class="services-modal-info">Brand Anthems & Overviews</p>',
    '<p class="services-modal-info">Web Page Development</p>': '<p class="services-modal-info">Executive Interviews</p>',
    '<p class="services-modal-info">Interactive UX/UI Creations</p>': '<p class="services-modal-info">Internal Communications</p>',
    '<p class="services-modal-info">Company Brand Positioning</p>': '<p class="services-modal-info">Event Highlight Reels</p>',
    '<p class="services-modal-info">Design and Mockup of products for companies</p>': '<p class="services-modal-info">Training & Onboarding Videos</p>',
    
    '<p class="services-modal-info">Usability Testing</p>': '<p class="services-modal-info">Fundraising Documentaries</p>',
    '<p class="services-modal-info">User Research</p>': '<p class="services-modal-info">Social Media Activism Stories</p>',
    '<p class="services-modal-info">Interaction Design</p>': '<p class="services-modal-info">Impact Reports</p>',
    '<p class="services-modal-info">Responsive Design</p>': '<p class="services-modal-info">Volunteer Spotlights</p>',
    '<p class="services-modal-info">Branding & Style Guides</p>': '<p class="services-modal-info">Campaign Teasers</p>',
    '<p class="services-modal-info">Accessibility</p>': '<p class="services-modal-info">Awareness Promos</p>',
    '<p class="services-modal-info">A/B Testing</p>': '<p class="services-modal-info">Grant Pitch Videos</p>',
    
    '<p class="services-modal-info">Competitive Analysis</p>': '<p class="services-modal-info">Advanced Color Grading</p>',
    '<p class="services-modal-info">Accessibility Design</p>': '<p class="services-modal-info">Professional Audio Sweetening</p>',
    '<p class="services-modal-info">Project Management</p>': '<p class="services-modal-info">Motion Graphics & Titles</p>',
    '<p class="services-modal-info">Iteration and Refinement</p>': '<p class="services-modal-info">Multi-Cam Editing</p>',
    '<p class="services-modal-info">Presenting Designs</p>': '<p class="services-modal-info">Format Optimization for Socials</p>',
    '<p class="services-modal-info">Surveys & Questionnaires</p>': '<p class="services-modal-info">Subtitling & Closed Captions</p>',
    
    'Working with Miriam was an absolute pleasure from start to finish. They took the time to truly understand our business needs and translated them into a stunning and highly functional website': 'Working with Tabitha was an absolute pleasure from start to finish. She took the time to truly understand our brand guidelines and translated them into a stunning corporate anthem video.',
    
    'Miriam truly understood our business needs through her modern and sleek design, making a site incredibly user-friendly. With her help, we had a significant increase in engagement and customer sales': "Tabitha truly understood our NGO's mission. Her documentary-style editing was incredibly moving. With her help, our latest fundraising campaign saw record-breaking donations.",
    
    "I was blown away by the website Miriam created for my business! Miriam crafted a incredibly user-friendly, that allows our customers to access information on any device. Since the launch, I've seen a significant increase in inquiries and bookings": "I was blown away by the promo video Tabitha edited for our launch! She crafted an incredibly high-energy sequence that perfectly matched our vision. Engagement skyrocketed immediately.",

    "Web Designer": "Corporate Video",
    "UI/UX Designer": "NGO Content",
    "Branding Designer": "Post-Prod & Grading"
}

for k, v in replacements.items():
    text = text.replace(k, v)

with codecs.open(html_path, "w", "utf-8") as f:
    f.write(text)

print("Semantic replacements complete.")
