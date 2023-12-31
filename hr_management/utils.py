import os
import barcode
from barcode.writer import ImageWriter
from django.conf import settings
import random
import string

def generate_barcode_data(starts_with:str='')->str:
    barcode_data = starts_with + ''.join(random.choice('0123456789') for _ in range(13-len(starts_with)))
    return barcode_data

def generate_barcode(barcode_data, directory_name):
    ean = barcode.get_barcode_class('ean13')
    ean_barcode = ean(barcode_data, writer=ImageWriter())
    full_directory_path = os.path.join(settings.BASE_DIR, directory_name)
    
    # Create the directory if it doesn't exist
    os.makedirs(full_directory_path, exist_ok=True)
    
    filename = barcode_data
    full_filepath = os.path.join(full_directory_path, filename)
    
    ean_barcode.save(full_filepath)
    return full_filepath

