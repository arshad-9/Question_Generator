import fitz
import easyocr
import tempfile

# Load OCR model once
reader = easyocr.Reader(['en'])


def extract_pdf_text(pdf_file):
    """
    Extract text from a PDF file.
    """

    text = ""

    pdf = fitz.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    for page in pdf:
        text += page.get_text()

    return text.strip()


def extract_image_text(image_file):
    """
    Extract text from image using EasyOCR.
    """

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".png"
    ) as temp_file:

        temp_file.write(image_file.read())

        results = reader.readtext(
            temp_file.name,
            detail=0
        )

    return " ".join(results).strip()


def is_image(filename):
    return filename.lower().endswith(
        (".jpg", ".jpeg", ".png")
    )