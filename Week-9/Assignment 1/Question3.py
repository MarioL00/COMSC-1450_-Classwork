def calculate_ticket_sales():
    total_sales = 0.0
    tickets_sold = 0

    while True:
        customer_age = int(input("Please input the customer's age or -1 to terminate: "))
        if customer_age == -1:
            break
        elif customer_age < 5:
           ticket_price = 0.0
        elif customer_age <= 12:
           ticket_price = 8.0
        elif customer_age <= 59:
            ticket_price = 12.0
        else:
            ticket_price = 9.0

        total_sales = total_sales + ticket_price
        tickets_sold = tickets_sold + 1

    if tickets_sold >= 10:
        total_sales = total_sales - (total_sales * 0.05)
    return total_sales, tickets_sold

def main():
    final_sales, tickets_sold = calculate_ticket_sales()

    print("Total tickets: ", tickets_sold)
    print("Final sales amount: ", final_sales)

main()