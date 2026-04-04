import re

files = ['index.html', 'testimonials.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the <youtube-embed> tags and extract URL
    # Replace shorts-grid with yt-grid
    content = content.replace('class="shorts-grid"', 'class="yt-grid"')
    
    def replace_yt(match):
        url = match.group(1)
        # Extract ID
        # https://youtube.com/shorts/E-YXVGLZ4gs?si=Duxw4wqchF8WZsd8
        vid = url.split('/shorts/')[1].split('?')[0]
        
        return f'''<a href="https://www.youtube.com/watch?v={vid}"
     target="_blank"
     rel="noopener"
     class="yt-card"
     aria-label="Watch Bhai Biryani Godown review on YouTube">
    <img
      src="https://img.youtube.com/vi/{vid}/hqdefault.jpg"
      alt="Bhai Biryani Godown review video Trichy"
      loading="lazy"
      width="480"
      height="360"
    />
    <div class="yt-play-badge">
      <svg viewBox="0 0 24 24" fill="white" width="24" height="24">
        <path d="M8 5v14l11-7z"/>
      </svg>
      Watch on YouTube
    </div>
  </a>'''

    # Replace <youtube-embed url="..." />
    content = re.sub(r'<youtube-embed url="([^"]+)"></youtube-embed>', replace_yt, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated YouTube elements.")
