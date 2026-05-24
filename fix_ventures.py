import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace specific instances
content = content.replace('href="#ventures">Ventures<', 'href="#projects">Projects<')
content = content.replace('href="#ventures"', 'href="#projects"')
content = content.replace('id="ventures"', 'id="projects"')
content = content.replace('<span>Ventures</span>', '<span>Projects</span>')

# Terminal strings
content = content.replace("'ventures'", "'projects'")
content = content.replace('"ventures"', '"projects"')
content = content.replace('ventures    :', 'projects    :')
content = content.replace('ventures: () =>', 'projects: () =>')
content = content.replace('// ventures', '// projects')
content = content.replace('about  experience  stack  ventures  clients', 'about  experience  stack  projects  clients')
content = content.replace("'venture'", "'project'")

with open('index.html', 'w') as f:
    f.write(content)

print("Ventures replaced with Projects")
