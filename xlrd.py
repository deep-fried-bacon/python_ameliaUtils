import xlrd




def xls2mat(path, sheet_index=0) :
    with xlrd.open_workbook(path) as wb :
        sheet = wb.sheets()[sheet_index]
        rows = []
        for i in range(sheet.nrows) :
            rows.append(sheet.row_values(i))
    return rows
    
#def xlrdWb2mat(path, sheet_index