password = input('Please enter your password:\n')
result = {}


digit_test = False
upper_test = False


if len(password) < 9:
    result['length'] = False
else:
    result['length'] = True

for c in password:
  #Check for digit
    digit = False
    for i in password:
        if i.isdigit():
            digit_test = True
        if i.isupper():
            upper_test = True

result['digit'] = digit_test
result['upper'] = upper_test
###
if all(result.values()) == False:
    print('Password does not meet all criteria')
else:
    print('password is strong, please continue')