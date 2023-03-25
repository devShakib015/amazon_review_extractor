import openpyxl

xlsx_file = 'input.xlsx'
txt_file = 'output.txt'

workbook = openpyxl.load_workbook(xlsx_file)
worksheet = workbook.active

with open(txt_file, 'w') as f:
    headerTitles = []
    for cell in worksheet[1]:
        headerTitles.append(cell.value)
    for row in worksheet.iter_rows(min_row=2):
        for cell in row:
            column_title = headerTitles[cell.col_idx - 1]
            row_content = str(cell.value)
            f.write(f"{column_title}:\n{row_content}\n\n")
        f.write(
            "\n\n----------------------------------------------------------------\n\n\n\n")
