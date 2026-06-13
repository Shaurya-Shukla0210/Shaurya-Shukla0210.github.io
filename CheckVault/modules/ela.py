from PIL import Image, ImageChops, ImageEnhance
import tempfile

def perform_ela(uploaded_file, quality=90):

    original = Image.open(uploaded_file).convert("RGB")

    temp_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)

    original.save(temp_file.name, "JPEG", quality=quality)

    compressed = Image.open(temp_file.name)

    diff = ImageChops.difference(original, compressed)

    extrema = diff.getextrema()

    max_diff = max([channel[1] for channel in extrema])

    if max_diff == 0:
        max_diff = 1

    scale = 255.0 / max_diff

    ela_image = ImageEnhance.Brightness(diff).enhance(scale)

    return ela_image