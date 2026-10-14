"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Information about a corporate bond.
# 2. Process: Create a dictionary, read its fields, update a value,
#    remove a field, and handle a missing key.
# 3. Out: The bond's information and its updated fields.
# 4. My object is a corporate bond. The five fields are issuer,
#    face value, coupon rate, maturity year, and credit rating.
#    These describe the issuer, payment terms, and credit risk.


# Your code below
bond = {
    "issuer": "Enel",
    "face_value": 1000,
    "coupon_rate": 4.5,
    "maturity": 2030,
    "credit_rating": "BBB+"
}

print("Corporate bond:", bond)
print("Bond issuer:", bond["issuer"])
print("Coupon rate (%):", bond["coupon_rate"])
print("Credit rating:", bond["credit_rating"])
bond["coupon_rate"] = 5.0

print("Updated coupon rate (%):", bond["coupon_rate"])
del bond["credit_rating"]

print("Bond after removing credit rating:", bond)
print("All remaining bond fields:")

for key, value in bond.items():
    print(key, ":", value)
# Accessing bond["currency"] would raise a KeyError.
# Using .get() allows the program to continue safely.
# Tested direct access to "currency": it raised a KeyError.
# Replaced it with .get() to handle missing keys safely.
currency = bond.get("currency", "Not available")

print("Bond currency:", currency)