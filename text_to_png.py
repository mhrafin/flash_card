from PIL import Image, ImageDraw, ImageFont, ImageTk


def to_png(text: str, color: tuple):
    font = ImageFont.truetype("font/arial.ttf", 60)

    image = Image.new("RGBA", (800, 100), (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(image)
    image_draw.text(
        (400, 50), text=text, anchor="mm", fill=color, font=font, direction="rtl"
    )

    tk_image = ImageTk.PhotoImage(image)

    # image.save("current_word.png")

    return tk_image
