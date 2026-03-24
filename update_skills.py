import codecs
import re

html_path = r"d:\website\portfolio\index.html"
with codecs.open(html_path, "r", "utf-8") as f:
    text = f.read()

new_skills_html = """
            <div class="skills-container container grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; padding: 2rem 0;">
                
                <div class="skills-data" style="display: flex; align-items: center; column-gap: 1rem; background-color: var(--box-color); padding: 1.5rem; border-radius: .5rem;">
                    <i class="uil uil-check-circle" style="color: var(--skin-color); font-size: 1.5rem;"></i>
                    <h3 class="skills-name" style="font-size: var(--normal-font-size);">Video Editing & Post-Production</h3>
                </div>

                <div class="skills-data" style="display: flex; align-items: center; column-gap: 1rem; background-color: var(--box-color); padding: 1.5rem; border-radius: .5rem;">
                    <i class="uil uil-check-circle" style="color: var(--skin-color); font-size: 1.5rem;"></i>
                    <h3 class="skills-name" style="font-size: var(--normal-font-size);">Storytelling for Social Impact</h3>
                </div>

                <div class="skills-data" style="display: flex; align-items: center; column-gap: 1rem; background-color: var(--box-color); padding: 1.5rem; border-radius: .5rem;">
                    <i class="uil uil-check-circle" style="color: var(--skin-color); font-size: 1.5rem;"></i>
                    <h3 class="skills-name" style="font-size: var(--normal-font-size);">Motion Graphics & Visual Effects</h3>
                </div>

                <div class="skills-data" style="display: flex; align-items: center; column-gap: 1rem; background-color: var(--box-color); padding: 1.5rem; border-radius: .5rem;">
                    <i class="uil uil-check-circle" style="color: var(--skin-color); font-size: 1.5rem;"></i>
                    <h3 class="skills-name" style="font-size: var(--normal-font-size);">Color Grading & Audio Enhancement</h3>
                </div>

                <div class="skills-data" style="display: flex; align-items: center; column-gap: 1rem; background-color: var(--box-color); padding: 1.5rem; border-radius: .5rem;">
                    <i class="uil uil-check-circle" style="color: var(--skin-color); font-size: 1.5rem;"></i>
                    <h3 class="skills-name" style="font-size: var(--normal-font-size);">Content Strategy for Digital Platforms</h3>
                </div>

                <div class="skills-data" style="display: flex; align-items: center; column-gap: 1rem; background-color: var(--box-color); padding: 1.5rem; border-radius: .5rem;">
                    <i class="uil uil-check-circle" style="color: var(--skin-color); font-size: 1.5rem;"></i>
                    <h3 class="skills-name" style="font-size: var(--normal-font-size);">Documentary & Advocacy Content Editing</h3>
                </div>

                <div class="skills-data" style="display: flex; align-items: center; column-gap: 1rem; background-color: var(--box-color); padding: 1.5rem; border-radius: .5rem;">
                    <i class="uil uil-check-circle" style="color: var(--skin-color); font-size: 1.5rem;"></i>
                    <h3 class="skills-name" style="font-size: var(--normal-font-size);">Social Media Video Optimization</h3>
                </div>

                <div class="skills-data" style="display: flex; align-items: center; column-gap: 1rem; background-color: var(--box-color); padding: 1.5rem; border-radius: .5rem;">
                    <i class="uil uil-check-circle" style="color: var(--skin-color); font-size: 1.5rem;"></i>
                    <h3 class="skills-name" style="font-size: var(--normal-font-size);">Creative Collaboration & Project Management</h3>
                </div>

            </div>
        </section>
"""

pattern = re.compile(r'(<section class="skills section" id="skills">\s*<h2 class="section-title" data-heading="">Core Skills</h2>).*?(<section class="work)', re.DOTALL)

text = pattern.sub(r'\g<1>\n' + new_skills_html + r'\n        \g<2>', text)

with codecs.open(html_path, "w", "utf-8") as f:
    f.write(text)

print("Skills replacement complete.")
