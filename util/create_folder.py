import os

def create_folder(nama_folder):
    if not os.path.exists(nama_folder):
        os.makedirs(nama_folder)
