def save_powers_to_file(filename):
    try:
        with open(filename, 'w') as file:
            file.write("Number,Square,Cube\n")

            for number in range(1, 101):
                square = number ** 2
                cube = number ** 3
                result = f"{number},{square},{cube}"

               
                print(result)

                file.write(result + "\n")

        print(f"Results saved to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")


save_powers_to_file("powers.txt")
