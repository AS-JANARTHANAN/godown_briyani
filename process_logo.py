from PIL import Image, ImageDraw

def process_logos(input_path):
    try:
        img = Image.open(input_path).convert("RGBA")
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # 1. Create bbg-logo-outline.png
    # Replace black with white, and white with transparent
    outline_img = Image.new("RGBA", img.size)
    pixels = img.load()
    out_pixels = outline_img.load()
    
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]
            # determine brightness
            brightness = (r + g + b) / 3
            if brightness > 128:
                out_pixels[x, y] = (255, 255, 255, 0) # Transparent
            else:
                out_pixels[x, y] = (255, 255, 255, a) # White

    outline_img.save("images/bbg-logo-outline.png")
    print("Created bbg-logo-outline.png")

    # 2. Update bbg-logo-filled.png (replace outer white corners with transparent)
    # We floodfill from 0,0 to make the outside transparent.
    # To do this safely, we will create a mask by floodfilling a copy.
    mask = Image.new('L', (width+2, height+2), 0)
    filled_img = img.copy()
    
    ImageDraw.floodfill(filled_img, (0, 0), (255, 255, 255, 0), thresh=50)
    ImageDraw.floodfill(filled_img, (width-1, 0), (255, 255, 255, 0), thresh=50)
    ImageDraw.floodfill(filled_img, (0, height-1), (255, 255, 255, 0), thresh=50)
    ImageDraw.floodfill(filled_img, (width-1, height-1), (255, 255, 255, 0), thresh=50)

    filled_img.save("images/bbg-logo-filled.png")
    print("Updated bbg-logo-filled.png")

if __name__ == "__main__":
    import os
    if os.path.exists("images/logo-filled.jpg"):
        process_logos("images/logo-filled.jpg")
    elif os.path.exists("images/bbg-logo-filled.png"):
        process_logos("images/bbg-logo-filled.png")
    else:
        # Search for any jpg/png that might correspond
        for f in os.listdir("images"):
            if f.endswith(("png", "jpg", "jpeg", "webp")):
                print("Found", f, "trying it...")
                process_logos(os.path.join("images", f))
                break
