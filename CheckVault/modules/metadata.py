from PIL import Image

def analyze_metadata(uploaded_file):

    metadata = {}

    try:
        image = Image.open(uploaded_file)

        metadata["format"] = image.format
        metadata["mode"] = image.mode
        metadata["size"] = image.size

        if hasattr(image, "_getexif") and image._getexif():
            metadata["exif_present"] = True
            metadata["exif_entries"] = len(image._getexif())
        else:
            metadata["exif_present"] = False

    except Exception as e:
        metadata["error"] = str(e)

    return metadata