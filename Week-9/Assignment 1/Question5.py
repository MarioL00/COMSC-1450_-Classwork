import math

def evaluate_advanced_piecewise(x):
    if x > 0:
        final_answer = math.sqrt(math.log10(x) + math.exp(x)) * math.cos(math.radians(x))
    elif x == 0:
        final_answer = 0.0
    else:
        final_answer = math.log(math.fabs(x)) + math.pow(math.fabs(x), 3)

    return final_answer

def main():
    x = float(input("Enter a value for x: "))
    final_answer = evaluate_advanced_piecewise(x)
    print("The final answer is: ", final_answer)

main()