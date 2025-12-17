from __future__ import annotations
import requests


def get_text(url: str, user_agent: str, timeout: int = 25) -> str:
    r = requests.get(url, headers={"User-Agent": user_agent}, timeout=timeout)
    r.raise_for_status()
    return r.text


def get_bytes(url: str, user_agent: str, timeout: int = 35) -> bytes:
    r = requests.get(url, headers={"User-Agent": user_agent}, timeout=timeout)
    r.raise_for_status()
    return r.content

