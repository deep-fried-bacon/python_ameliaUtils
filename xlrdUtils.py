import xlrd



# wb = xlrd.open_workbook(path)
    # wb --> xlrd.Workbook
# ws = xlrd.sheets()[sheet_index]
# ws_new = wb.new_sheet("sheet name", data=mat)
    # ws, ws_new --> xlrd.Worksheet
    
# ws.range([1,1],[10,10]).values = mat
    # same as data=mat in intialization


def xls2mat(path, sheet_index=0) :
    with xlrd.open_workbook(path) as wb :
        sheet = wb.sheets()[sheet_index]
        rows = []
        for i in range(sheet.nrows) :
            rows.append(sheet.row_values(i))
    return rows
    


    
def set_xls_range(sheet, rows, empty_row) :
    """ 
    sheet --> xlrd.Worksheet
    empty_row --> [int]
        int = first row that is empty
        empty_row is updated by set_xls_range
    """
    rows = autils.make_rec(rows)
    
    width = len(rows[0])
    height = len(rows)
        
    c_start = 1
    r_start = empty_row[0] 
    
    empty_row[0] += height

    c_end = c_start + width - 1
    r_end = r_start + height - 1
    
    xi = nums2xlsIndices([[r_start,c_start],[r_end,c_end]])
    sheet.range(xi[0],xi[1]).value = rows
    
    
    
    
    
    