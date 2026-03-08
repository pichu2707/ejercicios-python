age = int(input())
has_license = input() == "true"
has_insurance = input() == "true"

print(has_license)
print(has_insurance)
result = has_license and has_insurance and (age >= 18)
print(result)
