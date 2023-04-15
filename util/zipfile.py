import zipfile
import os

def Zipping(folderPath):
    zip_filename = folderPath + '.zip'
    zip_file = zipfile.ZipFile(zip_filename,'w',zipfile.ZIP_DEFLATED)

    # Menambahkan setiap file dalam folder ke file zip
    for root, dirs, files in os.walk(folderPath):
            for file in files:
                zip_file.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folderPath))
    zip_file.close()
    return zip_filename