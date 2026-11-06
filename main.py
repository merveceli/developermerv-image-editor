"""
developermerv-image-editor
by @developermerv | @merveceli
Fotoğraflara filtre, boyutlandırma ve imza ekleyen hafif editör
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
from pathlib import Path
import argparse

def add_watermark(image_path, text="developermerv", output_path=None):
    """Fotoğrafın sağ altına imza ekler"""
    img = Image.open(image_path).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (255,255,255,0))
    draw = ImageDraw.Draw(overlay)
    
    # Font boyutu görsele göre ayarlanır
    font_size = max(20, img.size[0] // 20)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # Sağ alt köşe
    bbox = draw.textbbox((0,0), text, font=font)
    x = img.size[0] - (bbox[2]-bbox[0]) - 20
    y = img.size[1] - (bbox[3]-bbox[1]) - 20
    
    # Yarı saydam arka plan
    draw.rectangle([(x-10, y-5), (x + (bbox[2]-bbox[0]) + 10, y + (bbox[3]-bbox[1]) + 5)], fill=(0,0,0,120))
    draw.text((x, y), text, font=font, fill=(255, 165, 0, 255)) # Turuncu imza
    
    combined = Image.alpha_composite(img, overlay)
    out = output_path or f"edited_{Path(image_path).name}"
    combined.convert("RGB").save(out)
    print(f"✅ İmza eklendi -> {out} | by developermerv")
    return out

def apply_filter(image_path, filter_type="bw", output_path=None):
    """Filtre uygular: bw, blur, sharpen, bright"""
    img = Image.open(image_path)
    if filter_type == "bw":
        img = img.convert("L")
    elif filter_type == "blur":
        img = img.filter(ImageFilter.BLUR)
    elif filter_type == "sharpen":
        img = img.filter(ImageFilter.SHARPEN)
    elif filter_type == "bright":
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.5)
    
    out = output_path or f"{filter_type}_{Path(image_path).name}"
    img.save(out)
    print(f"✅ Filtre ({filter_type}) uygulandı -> {out}")
    return out

def resize_image(image_path, width=1080, output_path=None):
    """Instagram için yeniden boyutlandırma"""
    img = Image.open(image_path)
    w_percent = (width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))
    img = img.resize((width, h_size), Image.LANCZOS)
    out = output_path or f"resized_{Path(image_path).name}"
    img.save(out)
    print(f"✅ Yeniden boyutlandırıldı {width}px -> {out}")
    return out

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="developermerv image editor")
    parser.add_argument("image", help="Fotoğraf yolu")
    parser.add_argument("--watermark", action="store_true", help="İmza ekle")
    parser.add_argument("--filter", choices=["bw","blur","sharpen","bright"], help="Filtre türü")
    parser.add_argument("--resize", type=int, help="Genişlik (px)")
    args = parser.parse_args()

    if args.watermark:
        add_watermark(args.image)
    if args.filter:
        apply_filter(args.image, args.filter)
    if args.resize:
        resize_image(args.image, args.resize)
    
    if not any([args.watermark, args.filter, args.resize]):
        # Varsayılan: hepsini yap
        print("🚀 developermerv-image-editor çalışıyor...")
        add_watermark(args.image)
