from PIL import Image
from PIL.ExifTags import TAGS

def view_image_metadata(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()

    if exif_data is not None:
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            print(f"{tag_name}: {value}")
    else:
        print("No metadata found.")

# Example usage
view_image_metadata("D:/Gskd-1.jpg")