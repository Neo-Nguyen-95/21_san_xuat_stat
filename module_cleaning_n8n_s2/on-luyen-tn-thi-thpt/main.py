import re
import os

def split_markdown_by_cau_pattern(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Pattern: 'Câu' + any chars (non-greedy) + a number + '.'
    pattern = r'(Câu.*?\d+\.)'
    parts = re.split(pattern, content, flags=re.DOTALL)
    
    result = []
    for i in range(1, len(parts), 2):
        block = parts[i] + (parts[i+1] if i+1 < len(parts) else '')
        result.append(block.strip())
    return result

def export_blocks_to_files(filepath):
    blocks = split_markdown_by_cau_pattern(filepath)

    base_name = os.path.basename(filepath)
    match = re.match(r'^(.+?)(_)(\d+)(\.md)$', base_name)
    if not match:
        raise ValueError('Filename does not match expected pattern.')
    prefix, sep, id_num, ext = match.groups()

    exported_count = 0
    for idx, block in enumerate(blocks, 1):
        if '$' not in block:
            continue  # Skip block with no '$'
        exported_count += 1
        new_name = f"{prefix}-{exported_count}{sep}{id_num}{ext}"
        with open(new_name, 'w', encoding='utf-8') as out_file:
            out_file.write(block)
        print(f"Wrote {new_name}")

# Example usage
# filepath = '12_on-luyen-tn-thi-thpt_cd1_28545799.md'
# export_blocks_to_files(filepath)
