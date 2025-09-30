"""
CISC 131 Problem 1 - Akhil Kanayinkal (kana9520) and Sean Marlow (marl9416)
"""

def main():
    """
    This function tests the insurancePremiumCalc function.
    """

    customer_count = 1000
    avg_claim_amount = 500
    percent_claims = 5

    #call the insurancePremiumCalc(...) function and store result in new variable
    premium = insurancePremiumCalc(customer_count, avg_claim_amount, percent_claims)

    #print "Average premium should be $xxx.xx in order to make $1,000,000 annually"

    print("Average premium should be $", end="")
    print(premium, "in order to make $1,000,000 annually.")

    #You should add more test cases to thoroughly test your function!

def insurancePremiumCalc(n_customers, claim_cost, claim_percentage):
    """
    This function calculates the annual premium insurance.
    """

    total = (n_customers * (claim_percentage/100)) * claim_cost
    total = (total + 1000000)/n_customers
    return total

main()
