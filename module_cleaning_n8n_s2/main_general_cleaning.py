import re
import unicodedata
from pathlib import Path
from typo_correction import get_correction_list
import os

def clean(file_path):    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # len(content)
    
    #%%% MODULE FIX TYPO
    def clean_typo(content):
        def split_protected_sections(content):
            # Tách LaTeX và ảnh: $...$, $$...$$, \[...\], ![...](...)
            pattern = re.compile(r"(\$\$.*?\$\$|\$.*?\$|!\[.*?\]\(.*?\))", re.DOTALL)
            return pattern.split(content)
        
        parts = split_protected_sections(content)
        
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
        
        text_corrected_typo = ''.join(corrected_parts)
        
        return text_corrected_typo
    
    text_corrected_typo = clean_typo(content)
    
    #%%% MODULE FIX MATH EQUATION
    def clean_math_latex(text):
        # Delete specific char
        text = text.replace(r'KQ: $\square$', '')
        text = re.sub(r'\[\]\(https?://[^\)]*\)', '', text)
        
        # Remove mathrm
        text = re.sub(r'\\mathrm\{([^}]*)\}', r'\1', text)
        
        # Use dfrac instead of frac    
        text = re.sub(r'\\frac(?=\s*{)', r'\\dfrac', text)
        
        text = (text
                .replace('$$', '$')
                .replace('##', '')
                # .replace('\n', ' ')
                )
        
        #    - Xóa khoảng trắng trước dấu câu
        text = re.sub(r'\s+([.,;:!?])', r'\1', text)
        
        #    - Xóa khoảng trắng thừa sau '(' và trước ')'
        text = re.sub(r'\(\s+', '(', text)
        text = re.sub(r'\s+\)', ')', text)
        
        #    - Gộp nhiều khoảng trắng liên tiếp thành một
        text = re.sub(r' {2,}', ' ', text)
        
        #    - Chuẩn hóa dấu ngoặc kép và dấu nháy đơn
        text = text.replace('“', '"').replace('”', '"')
        text = text.replace("‘", "'").replace("’", "'")
        
        
        return text
    
    text_corrected_math = clean_math_latex(text_corrected_typo)
    text_corrected_math[:1000]
        
    
    
    #%%% EXPORT
    filename = file_path
    
    with open(filename, "w", encoding="utf-8") as f:
            f.write(text_corrected_math)

#%%
folder_path = 'bo-de-on-tap-mon-toan-11-theo-cau-truc-moi-pham-le-duy/LT chương I toán 11/'
file_list = [os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path)]

for file in file_list:
    clean(file)


