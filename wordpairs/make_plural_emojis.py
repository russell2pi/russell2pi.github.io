from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

OUTPUT = Path("assets/plural-emojis")
OUTPUT.mkdir(parents=True, exist_ok=True)

SIZE = 512
BG = (255, 255, 255, 0)

FONT_PATH = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"

font = ImageFont.truetype(FONT_PATH, 109)

items = [
    ("horses", "🐎"),
    ("donkeys", "🫏"),
    ("stones", "🪨"),
    ("breads", "🍞"),
    ("pens", "🖊️"),
    ("camels", "🐪"),
    ("wolves", "🐺"),
    ("pigs", "🐖"),
    ("doors", "🚪"),
    ("houses", "🏠"),
    ("cups", "🥛"),
    ("sheep", "🐑"),
]


def draw_plural_emoji(filename, emoji, index):
    img = Image.new("RGBA", (SIZE, SIZE), BG)

    if index < 6:
        back_pos = (190, 90)
        front_pos = (90, 220)
    else:
        back_pos = (90, 130)
        front_pos = (170, 200)

    shadow_offset = (18, 18)

    shadow = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)

    shadow_draw.text(
        (back_pos[0] + shadow_offset[0], back_pos[1] + shadow_offset[1]),
        emoji,
        font=font,
        fill=(0, 0, 0, 120),
        embedded_color=True,
    )

    shadow_draw.text(
        (front_pos[0] + shadow_offset[0], front_pos[1] + shadow_offset[1]),
        emoji,
        font=font,
        fill=(0, 0, 0, 120),
        embedded_color=True,
    )

    shadow = shadow.filter(ImageFilter.GaussianBlur(10))
    img.alpha_composite(shadow)

    draw = ImageDraw.Draw(img)

    draw.text(back_pos, emoji, font=font, embedded_color=True)
    draw.text(front_pos, emoji, font=font, embedded_color=True)

    output_path = OUTPUT / f"{filename}.png"
    img.save(output_path)

    print(f"Saved {output_path}")


for index, (filename, emoji) in enumerate(items):
    draw_plural_emoji(filename, emoji, index)

print("Done.")
