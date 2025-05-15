import pandas as pd

#%% CHECK
# Define the expected columns based on A.xlsx (after skipping first 2 rows)
expected_columns = [
    'STT', 'Người soạn', 'Id', 'Nội dung câu hỏi', 'Đáp', 'Độ khó',
    'Loại câu hỏi', 'Kĩ năng', 'NL', 'Có sử dụng ảnh', 'Có sử dụng âm thanh', 'Thẻ'
]

def check_file_format(datapath):
    # Read the file, skipping metadata rows to get actual headers
    try:
        df = pd.read_excel(datapath, header=2)
    except Exception as e:
        return False, f"Error reading file: {e}"
    
    # Compare columns
    file_columns = list(df.columns)
    missing = [col for col in expected_columns if col not in file_columns]
    extra = [col for col in file_columns if col not in expected_columns]

    if not missing and not extra:
        return True, "Upload thành công!"
    else:
        return False, "Sai định dạng!"


#%% CONVERT
def transform_excel_to_stat(datapath):
    # Load A.xlsx, skipping first 2 rows for clean headers
    df = pd.read_excel(datapath, sheet_name=0, header=2)
    
    # Remove rows where "Kĩ năng" is missing (if any)
    df['Kĩ năng'] = df['Kĩ năng'].fillna("Bỏ trống")
    
    # Group by "Kĩ năng" and "Độ khó" and count occurrences
    summary = df.groupby(['Kĩ năng', 'Độ khó']).size().unstack(fill_value=0)
    
    # Ensure all columns for "Mức 1", "Mức 2", "Mức 3" are present
    for muc in ['Mức 1', 'Mức 2', 'Mức 3']:
        if muc not in summary.columns:
            summary[muc] = 0
    
    # Reorder columns and reset index for output
    summary = summary[['Mức 1', 'Mức 2', 'Mức 3']].reset_index()
    summary = summary.rename(columns={'Kĩ năng': 'Thành phần kiến thức'})
    
    summary.columns.name = None
    
    return summary


