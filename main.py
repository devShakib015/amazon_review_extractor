import openpyxl

xlsx_file = 'input.xlsx'
txt_file = 'output.txt'

workbook = openpyxl.load_workbook(xlsx_file)
worksheet = workbook.active

with open(txt_file, 'w') as f:

    worksheet.delete_cols(2, 2)
    worksheet.delete_cols(4, 5)

    headerTitles = []
    for cell in worksheet[1]:
        headerTitles.append(cell.value)
    for row in worksheet.iter_rows(min_row=2):
        for cell in row:
            column_title = headerTitles[cell.col_idx - 1]
            row_content = str(cell.value)

            if cell.col_idx == 1:
                star = row_content.split(" ")[0]
                row_content = f"{star} / 5.0"

            f.write(f"{column_title}:\n\n{row_content}\n\n\n")
        f.write(
            "\n\n----------------------------------------------------------------\n\n\n\n")
