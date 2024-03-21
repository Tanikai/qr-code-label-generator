from dataclasses import dataclass
import os
import jinja2
import blabel_src.label_tools as label_tools
import blabel_src.utils as blabel_utils
from typing import List
import json


context_tools = {
    "list": list,
    "len": len,
    "enumerate": enumerate,
    "qr_code": label_tools.qr_code,
    "str": str,
}

default_configuration = {
    "num_rows": 11,
    "num_columns": 4,
    "row_height": 25.5,  # in mm
    "column_width": 48.5,  # in mm
    "qr_code_height": 20,  # in mm
    "qr_code_margin": 2.5,
}


@dataclass
class InventoryLabel:
    asset_id: str
    base_url: str  # with trailing slash

    @property
    def asset_url(self) -> str:
        return f"{self.base_url}{self.asset_id}"

    def get_label_dict(self):
        return dict(asset_id=self.asset_id, asset_url=self.asset_url)


def generate_dicts_from_labels(labels: List[str], base_url: str):
    return [InventoryLabel(asset_id, base_url).get_label_dict() for asset_id in labels]


def generate_ids(sequence_start_hex: str, count: int):
    """Generate a sequence of hexadecimal ids."""
    sequence_start = int(sequence_start_hex, 16)
    return [f"{(sequence_start + i):0=5X}" for i in range(count)]


def load_config_file(config_path: str):
    with open(config_path, "r") as f:
        return json.load(f)


THIS_PATH = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(THIS_PATH, "data", "page_template.html"), "r") as f:
    PAGE_TEMPLATE = jinja2.Template(f.read())

context = dict(context_tools.items())
context.update(default_configuration)

config_path = os.path.join(THIS_PATH, "..", "config.json")
config_file = load_config_file(config_path)
context.update(config_file)

labels = generate_ids(f"0x{config_file['sequence_start']}", config_file["num_labels"])
context["labels"] = generate_dicts_from_labels(labels, config_file["base_url"])


html = PAGE_TEMPLATE.render(**context)  # get html file

with open(os.path.join(THIS_PATH, "data", "output.html"), "w") as f:
    f.write(html)

blabel_utils.write_pdf(
    html,
    target="label_sheet.pdf",
    base_url=context["base_url"],
    extra_stylesheets=("src/data/page_style.css",),
)
