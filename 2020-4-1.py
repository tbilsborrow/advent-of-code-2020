import sys

requiredfields = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}

count = 0
passportfields = set()
for line in sys.stdin:
    if not line.strip():
        # previous passport fully read in - now validate
        if requiredfields.issubset(passportfields):
            count += 1
        passportfields = set()
    else:
        # grab just field names from this line
        passportfields.update({v.split(':')[0] for v in line.split()})

# don't forget the last one
if requiredfields.issubset(passportfields):
    count += 1

print(count)
