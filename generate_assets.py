from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ASSETS_DIR = Path(__file__).resolve().parent / "assets"
ASSETS_DIR.mkdir(exist_ok=True)


def create_icon(path: Path):
    size = 256
    img = Image.new("RGBA", (size, size), "#0f172a")
    draw = ImageDraw.Draw(img)

    pad = 28
    body = (pad, pad, size - pad, size - pad)
    draw.rounded_rectangle(body, radius=42, fill="#111827", outline="#f97316", width=8)

    glove = [(80, 180), (120, 80), (180, 120), (200, 180), (172, 210), (120, 220)]
    draw.polygon(glove, fill="#f59e0b")
    draw.ellipse((100, 70, 165, 135), fill="#fef3c7")
    draw.ellipse((100, 145, 220, 205), fill="#ef4444")
    draw.rectangle((116, 130, 198, 160), fill="#f8fafc")
    draw.line((146, 128, 160, 80), fill="#f8fafc", width=8)
    draw.line((160, 80, 172, 120), fill="#f8fafc", width=8)
    draw.line((124, 190, 92, 230), fill="#f8fafc", width=10)
    draw.line((184, 190, 220, 230), fill="#f8fafc", width=10)
    draw.arc((70, 135, 150, 215), start=0, end=180, fill="#f8fafc", width=8)

    img.save(path)
    try:
        img.save(path.with_suffix(".png"), format="PNG")
    except Exception:
        pass


def create_splash(path: Path):
    width, height = 520, 240
    img = Image.new("RGBA", (width, height), "#0f172a")
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((10, 10, width - 10, height - 10), radius=22, fill="#111827", outline="#f97316", width=3)
    draw.rounded_rectangle((30, 30, width - 30, height - 30), radius=18, fill="#0b1220")

    for i in range(18):
        x = 40 + i * 24
        y = 60 + ((i % 3) * 8)
        draw.rectangle((x, y, x + 12, y + 50), fill="#f59e0b")

    draw.text((80, 100), "BOXMASTER PRO", fill="#f8fafc", font=ImageFont.truetype("arial.ttf", 36))
    draw.text((120, 150), "Kullanıma Hazır", fill="#34d399", font=ImageFont.truetype("arial.ttf", 22))
    img.save(path)


def main():
    icon_path = ASSETS_DIR / "boxmaster_icon.ico"
    splash_path = ASSETS_DIR / "boxmaster_splash.png"
    create_icon(icon_path)
    create_splash(splash_path)
    print(f"Asset oluşturuldu: {icon_path}")
    print(f"Splash ekranı oluşturuldu: {splash_path}")


if __name__ == "__main__":
    main()


