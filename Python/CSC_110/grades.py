def validate_age(age):
    if(age.isdigit() == False):
        return False
    if((len(age) < 10) and (float(age) < 111) and (float(age) >=0)):
        return True
    else:
        return False

def check_eligibility(age):
    if(age >= 18):
        return True
    else:
        return False



print( validate_age("20") ) # True
print( validate_age("20.5") ) # False
print( validate_age("20a") ) # False
print( validate_age("300") ) # False
print( check_eligibility(20) ) # True
print( check_eligibility(15) ) # False