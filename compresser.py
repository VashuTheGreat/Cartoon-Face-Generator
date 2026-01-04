from ipynbcompress import compress
saved = compress('Emoji_Face_Generator.ipynb', img_width=400, img_format='jpeg')  # Smaller width + JPEG for max shrink
print(f"Bytes saved: {saved}")
