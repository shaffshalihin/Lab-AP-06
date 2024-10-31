import re
def test_TI():
    pattern=r'^[a-zA-z2468]{40}[13579\s]{5}$'
    while True:
        test=input("= " )
        if re.match(pattern,test) :
            if len(test)==45:
                print("True")
                break
        else :
            print("False")
test_TI()