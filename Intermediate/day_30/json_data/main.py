# # FIleNotFound
#
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("Message is an error")

height = float(input("height: "))
weight = float(input("weight: "))

if height > 3:
    raise ValueError("Human height should be less then 3 meters")

bmi = weight / (height * height)
print(bmi)
