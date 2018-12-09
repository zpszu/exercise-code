friend_0 = {
    'first': 'wei',
    'last': 'xie',
    'age': 23,
    'city': 'yueyang',
}
friend_1 = {
    'first': 'qi',
    'last': 'wang',
    'age': 22,
    'city': 'hengyang',
}
friend_2 = {
    'first': 'ping',
    'last': 'long',
    'age': 23,
    'city': 'shenzhen',
}
people = [friend_0, friend_1, friend_2]

for friend in people:
    for key, value in friend.items():
        print(key + ": " + str(value))
    print("\n")
