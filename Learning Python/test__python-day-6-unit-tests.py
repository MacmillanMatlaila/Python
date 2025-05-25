from python-day-6-unit-tests import square

'''
def main():
    tes_square():
        
        
def test_square():
    
    '''
    if square(2) != 4:
        print ("2^2 was not 4")
    if square(3) != 9:
        print("3^2 was not 9")
     '''
    #Alternatively with no conditionals:
    assert square(2) == 4
    assert square(3) == 9
    
    #Alternatively with a print to help user:
    try:
        assert square(2) == 4
    except AssertionError:
        print("2^2 was not 4")
        
    try:
        assert square(3) == 9
    except AssertionError:
        print("3^2 was not 9")
    


if __name__=="__main__":
    main()
'''
     
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
