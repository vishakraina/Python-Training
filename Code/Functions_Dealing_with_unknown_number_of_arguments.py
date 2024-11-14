# Topic 46 - Functions: Dealing with an Unknown Number of Arguments

# Accepting Unknown Keyword Arguments (**kwargs)

def display_result(winner, score, **other_info):
    print("The winner was " + winner)
    print("The score was " + score)
    for key, value in other_info.items():
        print(key + ": " + value)

# Example call with extra keyword arguments
display_result(winner="Real Madrid", score="1-0", overtime="yes", injuries="none")
# Output:
# The winner was Real Madrid
# The score was 1-0
# overtime: yes
# injuries: none


# Accepting Unknown Positional Arguments (*args)

def display_nums(first_num, second_num, *opt_nums):
    print(first_num)
    print(second_num)
    print(opt_nums)

# Example call with extra positional arguments
display_nums(100, 200, 300, 400, 500)
# Output:
# 100
# 200
# (300, 400, 500)
