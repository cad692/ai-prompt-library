#!/usr/bin/env python3
"""Build the Index PDF (cover + prompt menu). No full prompt text."""

from __future__ import annotations

import io
from collections import defaultdict
from pathlib import Path

import qrcode
from reportlab.lib.colors import Color, HexColor, white, black
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
    Flowable,
)

ROOT = Path(__file__).resolve().parents[1]

BG = HexColor("#121212")
SURFACE = HexColor("#1A1A1A")
PRIMARY = HexColor("#2B6DEF")
INK = HexColor("#FFFFFF")
MUTED = HexColor("#A0A0A0")
LINE = HexColor("#2A2A2A")
BEGINNER = HexColor("#3DDC97")
INTERMEDIATE = HexColor("#F0A500")
ADVANCED = HexColor("#FF5C5C")

CAT_COLORS = {
    "assistants": HexColor("#1E3A8A"),
    "research": HexColor("#4C1D95"),
    "documents": HexColor("#1E4B7A"),
    "prompting": HexColor("#5B2C6F"),
    "presentations": HexColor("#7E4E1E"),
    "images-video": HexColor("#7A2E2E"),
    "work-business": HexColor("#1E5C3A"),
    "data-productivity": HexColor("#1F4E6B"),
    "addins": HexColor("#6B3A15"),
    "workflows": HexColor("#3D4A57"),
    "pakistan": HexColor("#0F6B5C"),
    "chains": HexColor("#1E3A8A"),
}


class DarkBackground(Flowable):
    """Paint full-page dark background once per page via onPage."""


def paint_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BG)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    # footer
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(18 * mm, 10 * mm, "Thrive Wellness & Development")
    canvas.drawRightString(A4[0] - 18 * mm, 10 * mm, f"Page {doc.page}")
    canvas.restoreState()


def style_sheet():
    return {
        "h1": ParagraphStyle(
            "h1", fontName="Helvetica-Bold", fontSize=24, textColor=INK, leading=28, spaceAfter=6
        ),
        "title": ParagraphStyle(
            "title", fontName="Helvetica-Bold", fontSize=9.5, textColor=INK, leading=12
        ),
        "usage": ParagraphStyle(
            "usage", fontName="Helvetica", fontSize=8, textColor=HexColor("#CFCFCF"), leading=10
        ),
        "link": ParagraphStyle(
            "link", fontName="Helvetica-Bold", fontSize=8.5, textColor=PRIMARY, leading=11, alignment=1
        ),
        "cat": ParagraphStyle(
            "cat", fontName="Helvetica-Bold", fontSize=10, textColor=INK, leading=12
        ),
        "body": ParagraphStyle(
            "body", fontName="Helvetica", fontSize=10, textColor=INK, leading=13, spaceAfter=3
        ),
        "muted": ParagraphStyle(
            "muted", fontName="Helvetica", fontSize=8.5, textColor=MUTED, leading=11
        ),
        "small": ParagraphStyle(
            "small", fontName="Helvetica", fontSize=8, textColor=MUTED, leading=10
        ),
        "eyebrow": ParagraphStyle(
            "eyebrow", fontName="Helvetica-Bold", fontSize=9, textColor=PRIMARY, spaceAfter=4
        ),
        "h2": ParagraphStyle(
            "h2", fontName="Helvetica-Bold", fontSize=13, textColor=INK, leading=16, spaceBefore=4, spaceAfter=4
        ),
        "jump": ParagraphStyle(
            "jump", fontName="Helvetica", fontSize=8, textColor=INK, leading=10
        ),
    }


def qr_image(url: str):
    qr = qrcode.QRCode(version=2, box_size=6, border=1)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#FFFFFF", back_color="#121212")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf


def difficulty_color(d: str):
    d = (d or "").lower()
    if d == "beginner":
        return BEGINNER
    if d == "advanced":
        return ADVANCED
    return INTERMEDIATE


def build_index_pdf(prompts, cfg) -> Path:
    from reportlab.platypus import Image as RLImage, HRFlowable

    styles = style_sheet()
    base = cfg["BASE_URL"].rstrip("/")
    out = ROOT / "downloads" / "AI-Prompt-Library-Index.pdf"
    out.parent.mkdir(exist_ok=True)

    doc = BaseDocTemplate(
        str(out),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=16 * mm,
        title="AI Prompt Library Index",
        author=cfg["workshop"]["org"],
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="dark", frames=[frame], onPage=paint_page)])

    story = []
    # --- Cover ---
    story.append(Paragraph("Thrive logo placeholder", styles["muted"]))
    story.append(Paragraph(cfg["workshop"]["org"], styles["body"]))
    story.append(Spacer(1, 5 * mm))
    story.append(Paragraph(f'{cfg["workshop"]["name"]} workshop', styles["eyebrow"]))
    story.append(Paragraph("AI Prompt Library", styles["h1"]))
    story.append(Paragraph(cfg["workshop"]["tagline"], styles["body"]))
    story.append(Spacer(1, 3 * mm))

    # CTA as link button table
    cta = Table(
        [[Paragraph(f'<link href="{base}/">Open the Prompt Library website →</link>', styles["link"])]],
        colWidths=[doc.width],
    )
    cta.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PRIMARY),
                ("TOPPADDING", (0, 0), (-1, -1), 12),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("BOX", (0, 0), (-1, -1), 0, PRIMARY),
            ]
        )
    )
    story.append(cta)
    story.append(Spacer(1, 5 * mm))

    qr_buf = qr_image(base + "/")
    qr_img = RLImage(qr_buf, width=28 * mm, height=28 * mm)
    qr_row = Table(
        [
            [
                qr_img,
                Paragraph(
                    "Scan to open the website on your phone.<br/><br/>"
                    f'<link href="{base}/"><font color="#2B6DEF">{base}/</font></link>',
                    styles["muted"],
                ),
            ]
        ],
        colWidths=[32 * mm, doc.width - 32 * mm],
    )
    qr_row.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    story.append(qr_row)
    story.append(Spacer(1, 6 * mm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE, spaceBefore=2, spaceAfter=8))
    story.append(Paragraph("How to use", styles["h2"]))
    story.append(
        Paragraph(
            "1. Find a prompt below and tap <b>Open</b>.<br/>"
            "2. Read the preview on the website.<br/>"
            "3. Tap <b>Copy</b> and paste it into your AI tool.",
            styles["body"],
        )
    )
    story.append(Spacer(1, 3 * mm))
    story.append(
        Paragraph(
            f'{len(prompts)}+ prompts · '
            f'<link href="{base}/pages/foundations.html"><font color="#2B6DEF">Foundations</font></link> · '
            f'<link href="{base}/pages/responsible.html"><font color="#2B6DEF">Responsible AI use</font></link> · '
            f'<link href="{base}/pages/cheat-sheet.html"><font color="#2B6DEF">Cheat sheet</font></link> · '
            f'<link href="{base}/downloads/offline-prompts.zip"><font color="#2B6DEF">Offline download</font></link>',
            styles["small"],
        )
    )

    # Category jump bar (labels only — PDF internal anchors are unreliable across viewers)
    story.append(Spacer(1, 4 * mm))
    jump_labels = " · ".join(c["short"] for c in cfg["categories"])
    story.append(Paragraph("Categories: " + jump_labels, styles["jump"]))
    story.append(
        Paragraph(
            f'Filter live on the website: <link href="{base}/"><font color="#2B6DEF">{base}/</font></link>',
            styles["small"],
        )
    )

    # Group prompts
    grouped = defaultdict(list)
    for p in prompts:
        grouped[p["category"]].append(p)

    for c in cfg["categories"]:
        items = grouped.get(c["id"], [])
        if not items:
            continue
        story.append(Spacer(1, 4 * mm))
        header = Table(
            [
                [
                    Paragraph(c["name"], styles["cat"]),
                    Paragraph(f'{items[0]["id"]} to {items[-1]["id"]}', styles["muted"]),
                ]
            ],
            colWidths=[doc.width * 0.7, doc.width * 0.3],
        )
        header.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), CAT_COLORS.get(c["id"], PRIMARY)),
                    ("TOPPADDING", (0, 0), (-1, -1), 7),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                ]
            )
        )
        # anchor via named destination roughly by keeping header
        story.append(header)

        rows = []
        for i, p in enumerate(items):
            open_url = f'{base}/?p={p["id"]}'
            diff_col = difficulty_color(p["difficulty"])
            left = Paragraph(
                f'<font color="#A0A0A0" size="8">{p["id"]}</font> <b><font size="9.5">{p["title"]}</font></b><br/>'
                f'<font size="8" color="#CFCFCF">{p["usage"]}</font>',
                styles["title"],
            )
            mid = Paragraph(
                f'<font color="#{diff_col.hexval()[2:] if hasattr(diff_col, "hexval") else "F0A500"}">'
                f'{p["difficulty"]}</font>',
                styles["small"],
            )
            # simpler difficulty paragraph
            mid = Paragraph(p["difficulty"], ParagraphStyle(
                f"d{p['id']}", fontName="Helvetica-Bold", fontSize=8, textColor=diff_col, leading=10, alignment=1
            ))
            right = Paragraph(
                f'<link href="{open_url}"><font color="#2B6DEF"><b>Open ↗</b></font></link>',
                styles["link"],
            )
            rows.append([left, mid, right])

        table = Table(rows, colWidths=[doc.width * 0.62, doc.width * 0.18, doc.width * 0.20])
        style_cmds = [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 3.5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
            ("LEFTPADDING", (0, 0), (-1, -1), 2),
            ("RIGHTPADDING", (0, 0), (-1, -1), 2),
            ("LINEBELOW", (0, 0), (-1, -2), 0.3, LINE),
            ("ALIGN", (1, 0), (1, -1), "CENTER"),
            ("ALIGN", (2, 0), (2, -1), "CENTER"),
        ]
        for i in range(len(rows)):
            if i % 2 == 1:
                style_cmds.append(("BACKGROUND", (0, i), (-1, i), HexColor("#181818")))
        table.setStyle(TableStyle(style_cmds))
        story.append(table)

    # Slightly denser body styles already set; rebuild
    doc.build(story)
    return out


if __name__ == "__main__":
    import yaml

    with open(ROOT / "config.yaml", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    with open(ROOT / "data" / "prompts.yaml", encoding="utf-8") as f:
        prompts = yaml.safe_load(f)["prompts"]
    path = build_index_pdf(prompts, cfg)
    print(path)
