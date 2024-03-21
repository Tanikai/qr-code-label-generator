# QR Code Label Generator

## About

This project generates IDs and their respective QR code (with a URL prefix) for
4785 label sheets (DIN A4). This can for example be used to inventory small
batches of items without buying a dedicated label printer, for example for your
home.

Currently, this project only supports incrementing hexadecimal numbers as IDs.

If you need support for other ID schemas or label sheet layouts, create an
issue and I'll look into it.

## Setup

For this project, you need a working Python 3 installation.

```bash
git clone https://github.com/Tanikai/qr-code-label-generator
cd qr-code-label-generator
pip install -r requirements.txt
```

**Attention**: You might need to install additional dependencies depending on
your platform, as this project uses *Weasyprint* to generate the PDF file.
[Read this documentation article on what dependencies you might need](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html).

## Configuration

```json
{
    "base_url": "https://example.com/", // with trailing flash
    "sequence_start": "AB001", // 5-character hexadecimal number
    "num_labels": 44 // 4785 label sheets have 44 labels
}
```

Layouts, margins, etc. can be configured as well:

```json
todo
```

## Usage

Just call the `main.py` script with python:

```bash
python src/main.py
```

## Example

[The current configuration generates a sheet like this.](example/sheet.pdf)

## License

This project is licensed under MIT License and is derivative work of
[Blabel](https://github.com/Edinburgh-Genome-Foundry/blabel).
