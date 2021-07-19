# learning logical operator like AND , OR , NOT
# AND is used when both condition is true
# OR is used when one of the condition is true
#NOT is used to invert TRUE to FALSE and vice versa

has_good_credit = True
has_good_income = True

if has_good_credit and has_good_income:
    print("You are eligible for loan")

has_good_credit = False
has_good_income = True

if has_good_credit or has_good_income:
    print("You are eligible for loan")


has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("You are eligible for loan")