from paddleocr import PaddleOCR

# Initialize OCR once
ocr = PaddleOCR(use_angle_cls=True, lang='en')


def run_ocr(image_path: str) -> str:
    """
    Runs OCR on an image and returns extracted text as a single string.
    """
    result = ocr.ocr(image_path, cls=True)

    lines = []

    for line in result[0]:
        text = line[1][0]
        lines.append(text)

    return "\n".join(lines)
