correct_password = "PYTHON"
while True:
    user_input = input("Enter password: ")
    if user_input == correct_password:
        print("Login Sucessful! :)")
        break
    else:
        print("Incorrect password, try again.")
#Convert a 2D list into a flat 1D list using list comprehension.
list_2D = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in list_2D for item in sublist]
print(flat)
#Given a string, use list comprehension to create a list of all characters, excluding vowels.
s="HelloWorld"
vowels='aeiouAEIOU'
result=[char for char in s if char not in vowels]
print(result)
#From a given list of words, extract only those that start with a vowel (a, e, i, o, u).
 #            Example:
   #           words = ["functions", "loops", "oops", "exception", "as"]
words=["functions", "loops", "oops", "exception", "as"]
vowels='aeiouAEIOU'
print(result)