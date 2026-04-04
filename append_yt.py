with open('main.js', 'a', encoding='utf-8') as f:
    f.write('''\n/* ????????????????????????????????????????????
   REUSABLE YOUTUBE EMBED COMPONENT
???????????????????????????????????????????? */
class YouTubeEmbed extends HTMLElement {
  connectedCallback() {
    this.rawUrl = this.getAttribute('url');
    this.videoId = this.extractId(this.rawUrl);
    
    // Fallback detection logic
    if (!this.videoId) {
      this.innerHTML = '<div style="position:absolute;top:0;left:0;width:100%;height:100%;background:#1c1c14;border-radius:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:20px;text-align:center;"><p style="color:#f5f0e0;margin-bottom:16px;font-size:14px;">Invalid Video Link</p><a href="' + this.rawUrl + '" target="_blank" style="background:#F5CB00;color:#121210;padding:10px 20px;border-radius:24px;font-weight:bold;text-decoration:none;font-size:14px;">Watch on YouTube</a></div>';
      return;
    }

    this.renderIframe();
  }

  extractId(url) {
    if (!url) return null;
    const regExp = /^.*(youtu\.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=|shorts\/)([^#\&\?]*).*/;
    const match = url.match(regExp);
    return (match && match[2].length === 11) ? match[2] : null;
  }

  renderIframe() {
    const embedUrl = 'https://www.youtube.com/embed/' + this.videoId;
    
    this.classList.add('short-wrap');
    this.style.display = 'block';
    
    this.innerHTML = 
      <!-- Loading Skeleton -->
      <div class="yt-skeleton" style="position:absolute;top:0;left:0;width:100%;height:100%;background:#1c1c14;border-radius:16px;display:flex;align-items:center;justify-content:center;z-index:1;">
         <div style="width:40px;height:40px;border:3px solid rgba(255,215,0,0.3);border-top-color:#F5CB00;border-radius:50%;animation:spin 1s linear infinite;"></div>
      </div>
      
      <!-- Video Iframe -->
      <iframe 
        src="" 
        title="YouTube Video" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen 
        loading="lazy"
        onload="this.previousElementSibling.style.display='none';"
        style="position:absolute; top:0; left:0; width:100%; height:100%; border:none; z-index:2; border-radius:16px;">
      </iframe>
    ;

    if (!document.getElementById('yt-spin-style')) {
      const style = document.createElement('style');
      style.id = 'yt-spin-style';
      style.innerHTML = '@keyframes spin { to { transform: rotate(360deg); } }';
      document.head.appendChild(style);
    }
  }
}
customElements.define('youtube-embed', YouTubeEmbed);
''')
