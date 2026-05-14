from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

BG    = (30, 80, 50)    # verde oscuro
FG    = (255, 255, 255) # blanco
SIZES = {"icon-192.png": 192, "icon-512.png": 512}

for filename, size in SIZES.items():
    img  = Image.new("RGB", (size, size), BG)
    draw = ImageDraw.Draw(img)

    # Radio de esquinas redondeadas
    r = size // 6
    mask = Image.new("L", (size, size), 0)
    md   = ImageDraw.Draw(mask)
    md.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=255)
    img.putalpha(mask)

    # Texto CMR — busca una fuente del sistema, cae a default si no encuentra
    font_size = size // 3
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", font_size)
    except Exception:
        font = ImageFont.load_default(size=font_size)

    bbox = draw.textbbox((0, 0), "CMR", font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size - tw) / 2 - bbox[0]
    y = (size - th) / 2 - bbox[1]
    draw.text((x, y), "CMR", fill=FG, font=font)

    # Guardar como RGBA → PNG con transparencia en esquinas
    img.save(filename)
    print(f"  {filename} ({size}x{size})")

print("Íconos generados.")
