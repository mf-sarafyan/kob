from __future__ import annotations
from bs4 import BeautifulSoup
from src.wiki_importer.extractor.wiki_page import ExtractedPage, ImageCandidate
from src.wiki_importer.utils.http import get_text


def extract_fandom_page(url: str, user_agent: str, source_name: str) -> ExtractedPage:
    html = get_text(url, user_agent=user_agent)
    soup = BeautifulSoup(html, "html.parser")

    # Title
    title = None
    og_title = soup.find("meta", property="og:title")
    if og_title and og_title.get("content"):
        title = og_title["content"]
    if not title and soup.title:
        title = soup.title.get_text().strip()
    title = (title or "Untitled").replace(" | Fandom", "").strip()

    # Images: infobox first, then og:image
    images: list[ImageCandidate] = []

    infobox_img = soup.select_one("figure.pi-item img")
    if infobox_img:
        src = infobox_img.get("src") or infobox_img.get("data-src")
        if src:
            images.append(ImageCandidate(url=src, kind="infobox"))

    og_image = soup.find("meta", property="og:image")
    if og_image and og_image.get("content"):
        images.append(ImageCandidate(url=og_image["content"], kind="og"))

    # Text extraction (simple)
    # Fandom main content often in .mw-parser-output
    content = soup.select_one(".mw-parser-output")
    raw_text = content.get_text("\n", strip=True) if content else soup.get_text("\n", strip=True)

    return ExtractedPage(
        title=title,
        source_name=source_name,
        source_url=url,
        raw_text=raw_text,
        image_candidates=images,
    )

