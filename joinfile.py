from PyPDF2 import PdfFileMerger
import os
def pathfile(path):
    merger = PdfFileMerger()

    path_to_files = path

    for root, dirs, file_names in os.walk(path_to_files):
        for file_name in file_names:

            merger.append(path_to_files + file_name)
    merger.write(path+"youneedthisone.pdf")
    merger.close()