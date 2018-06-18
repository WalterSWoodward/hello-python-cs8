# To run this, follow these instructions:
# Run `pipenv --three` inside repository
#   # `three` denotes python 3
#   # Then terminal `pipenv shell`
# To actually RUN: terminal `python src/hello_python.py` (* while INSIDE pipenv shell)

greeting_f = 'Bonjour Monde!'
greeting_j = 'Konichiwa Sekai!'
greeting = 'Hello World!'

num = 12
arr = [1, 2, 3, 4]

# print("\nGreeting in Japenese is:", greeting_j)
# print("\nnum:", num)
# print("\nThe length of arr is:", len(arr), "\n")

a = 1
b = 'this is a string'

# APPEND
# c = [1, 2, 3, 4]
# d = 5, 6, 7, 8
# print(c)
# c.append(d)
# print(c) # weird!


# KEY VALUE PAIRS
# e = {'name': 'Walter', 'age': 29, 'number': 1}

# print("\nMy name is ", e['name'], "...")
# print("\n...and I am ", e['age'], "years old!", "\n")

# LOOP
# e = {'number': 1}

# c = [1, 2, 3, 4]
# d = 5, 6, 7, 8 # works even though this is not inside brackets!
# e['number'] += 9000
# print(e['number'])

# for n in c:
#     for m in d:
#         print(n*m)

#
def count_to_one_ten():
    # range is first- inclusive, last-exclusive, hence `11`
    for x in range(1, 11):
        print(x)


def done():
    print('Done!')


if __name__ == "__main__":
    # functions called here:
    count_to_one_ten()
    done()

    # You CAN do it this way, but it NOT considered best practice!
    # for x in range(1, 10):
    #     print(x)
    # print('Done!')
