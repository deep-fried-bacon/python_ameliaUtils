# at some point turn this into a 2darr class

# changes to some names
# arr --> 1d list
# mat --> 2d lists --> list of lists



    # 2d array (arr2d) --> a list of lists
    # inner_arrs are represented by each list (within the list), let's call them "rows"
    # faux_arrs are the "columns"
        # they are the datasets represented by taking the element at some position from each inner_arr
        # arr2d[:][<position>]

"""
arr ->  array ->    list -->            []
mat ->  matrix ->   list of lists -->   [[]]

rows --> mat where inner_arrs(inner lists) represent rows
cols --> mat where inner_arr(innner lists) represent columns
"""


import csv
import codecs
import copy
import math
import numbers

class LengthError(Exception) :
    def __init__(self, message) :
        Exception.__init__(self, message)
        
        
def print_types(obj,tc=0) :
    """prints out the type of an object and the type of containing objects for containers
    """
    if isinstance(obj, dict):
        print("\n" + (tc*"  ") + "dict{", end="")
        for v in obj.values() :
            print_types(v, tc+1)
        print("}" + (tc*"  ") + "\n" ,end="")
    elif isinstance(obj, list) :
        print("\n" + (tc*"  ") + "list[", end="") 
        for item in obj :
            print_types(item,tc+1)
        print("]\n" + (tc*"  ") ,end="")
    else :
        print(obj.__class__.__name__ + ",", end="")


def calc_dist(coords1, coords2) :
    """ calculates the distance between to coordinates
    
    (coords1, coords2) 
        --> ((x1,y1),(x2,y2))
        --> ([x1,y1],[x2,y2])
    """
    xdif = coords1[0] - coords2[0]
    ydif = coords1[1] - coords2[1]

    return (math.sqrt(xdif*xdif + ydif*ydif))

def calc_avg(arr) :
    """calculates average of numbers in an array"""
    if len(arr) == 0 :
        return None
    sum = 0
    for num in arr :
        if num != None :
            sum += num
    return (sum/len(arr))

    
def csv2rows(path,item_type=type("aaa")) :
    """read a csv file to a rowsrix of rows (inner_arrs are rows in csv file)
    
    item_type --> where possible, all elements are converted to this type,
        if item_type == None, no conversion is done
        
        item_type = type("aaa") --> str
        item_type = type(1.1) --> float
        item_type = type(1) --> int
    """
    rows = []
    with open(path, "r") as csvfile :
        my_reader = csv.reader(csvfile)
        for row in my_reader :
            rows.append(row)
    
    # if there's a BOM_UTF8 at the beginning of the file, remove it
    if rows[0][0].startswith("ï»¿") :
        rows[0][0] = rows[0][0][3:]
    
    
    test_count = 0
    # where possible, converts all elements to item_type
    if item_type != None :
        for r in range(len(rows)) :
            test_count += 1
            for c in range(len(rows[r])) :
                try :
                    rows[r][c] = item_type(rows[r][c])
                    
                    # if test_count < 10 : 
                        # temp = rows[r][c]
                        # temp2 = float(temp)
                        # print(temp2, end=", ")
                        # print(type(temp2))
                        
                except :
                    pass
    return rows
    
def rowIsEmpty(row, emptyTypes=['']) :
    for item in row :
        for emptyType in emptyTypes :
            if not item == emptyType :
                return False
    return True

def mat2csv(mat,path,mode="a") :
    with open(path, mode) as csvfile :
        my_writer = csv.writer(csvfile, lineterminator="\n")
        for arr in mat :
            my_writer.writerow(arr)
           #my_writer.writerow(", ".join(arr))
    return    


    # calls make_rec on mat1 which changes the orignal
def rotate(mat1,blank=None) :
    """takes a 2d array and swaps the 'columns' and 'rows' - 
    or swaps the 'inner_arrs' with the 'faux_arrs'"""
    mat1 = make_rec(mat1,blank=blank)
    print(mat1)
    mat2 = []
    for i in range(0,len(mat1[0])) :
        mat2.append([arr[i] for arr in mat1])
    return mat2
    
def rotate_no_orig_change(mat,blank=None) :
    """rotates(transposes) a matrix
    takes a 2d array and swaps the 'columns' and 'rows' - 
    or swaps the 'inner_arrs' with the 'faux_arrs'"""
    mat1 = make_rec(mat,blank=blank)
    mat2 = []
    for i in range(0,len(mat1[0])) :
        mat2.append([arr[i] for arr in mat1])
    return mat2
    
def rotate(mat, blank=None) :
    if is_rec(mat) :
        mat1 = mat
    else :
        mat1 = copy.deepcopy(mat)
     
    make_rec(mat1,blank=blank)
    mat2 = [[arr[i] for arr in mat1] for i in range(len(mat1[0]))]
    return mat2
    

def is_rec(mat) :
    length = len(mat[0])
    for arr in mat[1:] :
        if len(arr) != length :
            return False
    return True
        

    # alters orignal mat
def make_rec(mat, blank=None) :
    longest = 0
    check = False
    for inner_arr in mat :
        if longest < len(inner_arr) :
            check = True
            longest = len(inner_arr)
    
    if check :
    
        for inner_arr in mat :
            while len(inner_arr) < longest :
                inner_arr.append(blank)
    # return unneccesary? mat(lists) --> mutable
    #return mat
    
    

    
    
def print_mat(mat,  num_format="{0:.2f}") :
    """prints out a matrix with each arrar on a newline
    
    num_format --> format all numbers are printed with
        by default 2 decimal places
    """
    for arr in mat :
        for item in arr :
            if isinstance(item,numbers.Number) :
                print(num_format.format(item), end=", ")
            else :
                print(item, end=", ")
        print("")
        
def print_arr(arr) :
    """prints out an array with each item on a newline"""
    for item in arr :
        print(item)
        
        
        

# index_start can only be 0 or 1
def num2alpha(n,index_start=1) :
    """Takes a number and returns its "spreadsheet" alphabet equivalent.
    
    num2alpha(1) -> 'A'
    num2alpha(27) -> 'AA'
    num2alpha(42) -> 'AP'
    num2alpha(120) -> 'DP'
 
    index_start -> is n using 1-based indices or 0-based? 
        can only be 0 or 1
    """
    
    if index_start == 0 :
        n+=1
    elif index_start != 1 :
        msg = ()
        raise ValueError('index_start must be equal to 0 or 1.Recieved {}.'.format(index_start))
    
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string