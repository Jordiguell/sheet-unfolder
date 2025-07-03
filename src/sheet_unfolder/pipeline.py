from pathlib import Path
from .ingest.pdf_scanner import scan_pdf
from .bom.bom_parser import extract_bom
from .geometry.segment_graph import build_graph
from .geometry.unfold import unfold_panels
from .export.dxf_writer import write_dxf_by_thickness


def process_plan(pdf_path: Path, out_dir: Path) -> None:
    """Pipeline completa però encara amb mòduls stub."""
    pages = scan_pdf(pdf_path)          # Estructura amb .bom i .views
    bom   = extract_bom(pages.bom)      # DataFrame o llista de dicts
    graphs = [build_graph(p) for p in pages.views]
    unfolds = [unfold_panels(g) for g in graphs]
    write_dxf_by_thickness(unfolds, bom, out_dir)
