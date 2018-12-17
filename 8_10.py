#
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    magician_great = []
    while magicians:
        magic_great = "the Great " + magicians.pop()
        magician_great.append(magic_great)
    return sorted(magician_great)


magician = ['A', 'B', 'C']
great_magician = make_great(magician)
show_magicians(great_magician)
