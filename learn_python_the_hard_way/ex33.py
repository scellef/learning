def build_list(num, inc):
    # i = 0
    numbers = []

    # while i < num
    for i in range(0, num, inc):
        print "At the top i is %d" % i
        numbers.append(i)

        # i += inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for number in numbers:
        print number

print "How big of a list do you want? "
list_size = input("> ")

print "How many steps at a time will you take? "
inc_size = input("> ")

build_list(list_size, inc_size)
