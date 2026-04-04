import sys

with open('styles.css', 'rb') as f:
    raw = f.read()

content = raw.decode('utf-8', errors='ignore')

old_grid = '''.yt-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  padding: 0 16px;
  overflow-x: auto;
}

.yt-grid .yt-card {
  min-width: 150px;
}'''

new_grid = '''.yt-grid {
  display: flex;
  gap: 16px;
  padding: 0 16px 24px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;
}

.yt-grid::-webkit-scrollbar {
  display: none;
}

.yt-grid .yt-card {
  flex: 0 0 calc(85% - 16px);
  min-width: 250px;
  scroll-snap-align: center;
}

@media (min-width: 768px) {
  .yt-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    overflow-x: visible;
  }
  .yt-grid .yt-card {
    flex: auto;
    min-width: 0;
  }
}'''

content = content.replace(old_grid, new_grid)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"CSS replaced successfully.")
