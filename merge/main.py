import glob
from PyPDF2 import PdfFileMerger
import os
import logging

logging.basicConfig(filename='log.log',
                    level=logging.INFO,
                    format='%(asctime)s |  %(levelname)s | %(message)s')

DEFAULT_PDF_NAME = "Projekt"


def merge():
    pdfs = get_all_pdfs()
    merger = PdfFileMerger(strict=False)
    for pdf in pdfs:
        merger.append(pdf)
    new_name = create_new_name(pdfs[0])
    new_dir = create_new_folder(new_name)
    new_path = os.path.join(new_dir, new_name+".pdf")
    merger.write(new_path)
    os.startfile(new_path)
    merger.close()


def get_all_pdfs():
    pdf_files = glob.glob("*.pdf")
    return pdf_files


def create_new_name(file=None):
    try:
        return file.split(" ")[1]
    except:
        return DEFAULT_PDF_NAME


def create_new_folder(new_folder):
    try:
        os.mkdir(new_folder)
    except Exception as e:
        logging.error(e)
    return new_folder


if __name__ == '__main__':
    merge()
