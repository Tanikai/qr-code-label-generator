from weasyprint import HTML
import qrcode
import base64
from io import BytesIO


def write_pdf(html, target=None, base_url=None, extra_stylesheets=()):
    """Write the provided HTML in a PDF file.

    Parameters
    ----------
    html
      A HTML string

    target
      A PDF file path or file-like object, or None for returning the raw bytes
      of the PDF.

    base_url
      The base path from which relative paths in the HTML template start.

    use_default_styling
      Setting this parameter to False, your PDF will have no styling at all by
      default. This means no Semantic UI, which can speed up the rendering.

    extra_stylesheets
      List of paths to other ".css" files used to define new styles or
      overwrite default styles.
    """
    weasy_html = HTML(string=html, base_url=base_url)
    if target in [None, "@memory"]:
        with BytesIO() as buffer:
            weasy_html.write_pdf(buffer, stylesheets=extra_stylesheets)
            pdf_data = buffer.getvalue()
        return pdf_data
    else:
        weasy_html.write_pdf(target, stylesheets=extra_stylesheets)
