def main():
    purchase_count = int(input())

    if purchase_count == 0:
        print("Nenhuma compra registrada.")
    else:
        total_spent = 0.0
        i = 1

        while i <= purchase_count:
            try:
                purchase_value = float(input())
            except ValueError:
                continue  

            if purchase_value < 0:
                continue  
            else:
                total_spent += purchase_value
                i += 1

        # TODO: Calcule a média
        average_purchase = total_spent / purchase_count

        print(f"{total_spent:.2f}")
        print(f"{average_purchase:.2f}")

if __name__ == "__main__":
    main()