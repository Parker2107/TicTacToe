from project import check_winner, is_full, print_board

def test_check_winner():
    assert check_winner([['X','X','X'],[' ','O',' '],[' ','O','O']],'X')==True
    assert check_winner([['X',' ','X'],[' ','O',' '],[' ','O','O']],'X')==False
    assert check_winner([['X',' ',' '],['X','O',' '],['X','O','O']],'X')==True
    assert check_winner([['X','O',' '],['X','O','X'],[' ','O','O']],'O')==True

def test_is_full():
    assert is_full([['X','X','X'],[' ','O',' '],[' ','O','O']])==False
    assert is_full([['X',' ','X'],[' ','O',' '],[' ','O','O']])==False
    assert is_full([['X','X','X'],['O','O','O'],['O','O','O']])==True
    assert is_full([['X','X','O'],['O','X','X'],['X','O','O']])==True

def test_print_board():
    assert print_board([['X','X','X'],[' ','O',' '],[' ','O','O']])==True
