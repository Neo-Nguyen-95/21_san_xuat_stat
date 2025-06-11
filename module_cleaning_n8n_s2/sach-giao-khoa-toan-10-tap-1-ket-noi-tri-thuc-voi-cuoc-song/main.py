import re
import unicodedata
from pathlib import Path
from typo_correction import get_correction_list

#%% EDA
def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

file_path = 'sach-giao-khoa-toan-10-tap-1-ket-noi-tri-thuc-voi-cuoc-song_cut.md'
md_content = read_md_file(file_path)
md_content = md_content.lower()

len(md_content)

#%% CLEAN LINK
md_content = re.sub(r'!\[\]\([^)]+\)', '', md_content)

#%% FIX TYPO
def split_protected_sections(content):
    # Tách LaTeX và ảnh: $...$, $$...$$, \[...\], ![...](...)
    pattern = re.compile(r"(\$\$.*?\$\$|\$.*?\$|!\[.*?\]\(.*?\))", re.DOTALL)
    return pattern.split(content)

parts = split_protected_sections(md_content)

def fix_vietnamese_typos(s):
    s = unicodedata.normalize("NFC", s)
    corrections = get_correction_list()
    for wrong, right in corrections.items():
        s = s.replace(wrong, right)
    return s

corrected_parts = [
    fix_vietnamese_typos(part) if i % 2 == 0 else part
    for i, part in enumerate(parts)
]

corrected_text = ''.join(corrected_parts)

#%% SPLIT TEXT

sections = re.split(
    r"(?=## bài\s+\d+|## bài tập)",
    corrected_text, flags=re.IGNORECASE
    )
# Remove empty sections, if any
sections = [sec.strip() for sec in sections if sec.strip()]


for i, section in enumerate(sections):
    file_name = str(i+1) + section.split('\n')[0] + '.md'
    Path(file_name).write_text(section.strip(), encoding="utf-8")



