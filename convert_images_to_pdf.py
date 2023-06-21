import os
from PIL import Image

def convert_png_to_pdf(png_path, pdf_path):
    image = Image.open(png_path).convert("RGB")
    image.save(pdf_path, "PDF", resolution=100.0)

def convert_folder_to_pdf(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".png"):
            png_path = os.path.join(folder_path, file_name)
            pdf_path = os.path.splitext(png_path)[0] + ".pdf"
            convert_png_to_pdf(png_path, pdf_path)

# Directory
#folder = "\home\path"  \\For Linux
folder = r"C:\Users\path"  \\For Windows
convert_folder_to_pdf(folder)
