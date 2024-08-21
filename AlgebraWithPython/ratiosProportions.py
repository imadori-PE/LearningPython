# converts string input (even fractions) to float
def string_frac(in_string):
    if "/" in in_string:
        nd = in_string.split("/")
        n = float(nd[0])
        d = float(nd[1])
        ans = n/d
        return ans
    else:
        ans = float(in_string)
        return ans


# Simplest one-step addition
def one_step_add():
    import random
    # Display problem
    a = random.randint(-4,10)
    b = random.randint(2,24)
    print("x + ", a, " = ", b)
    ans = float(input("x = "))
    answer = b-a
    # Test input
    if ans==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")


# One-step additon with negaive numbers
def one_step_subtract():
    import random
    a = random.randint(-19,-1)
    b = random.randint(2,24)
    print(a, " + x = ", b)
    ans = float(input("x = "))
    # test
    answer = b-a
    if ans==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")

# One-step multiply
def one_step_mult():
    # Uses string_frac(<input string>)
    import random
    a = random.randint(1,11)
    b = random.randint(2,24)
    print(a, "x = ", b)
    print("Round your answer to two decimal places.")
    ans_in = (input("x = "))
    answer = round(b/a,2)
    # test
    if string_frac(ans_in)==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")


# One-step divide
def one_step_div():
    import random
    a = random.randint(1,11)
    b = random.randint(2,24)
    print("x/", a, " = ", b)
    ans = float(input("x = "))
    answer = b*a
    # test
    if ans==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")


# Two-step problems
def two_step():
    import random
    # Uses string_frac()
    a = random.randint(1,11)
    b = random.randint(-7,12)
    c = random.randint(2,36)
    print(a, "x + ", b, " = ", c)
    print("Round answer to two decimal places")
    ans_in = input("x = ")
    answer = (c-b)/a
    # test
    if round(string_frac(ans_in),2)==round(answer,2):
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")


# test loop
for a in range(2):
    one_step_add()
    one_step_subtract()
    one_step_mult()
    one_step_div()
    two_step()
    print(" ")

two_step()
two_step()