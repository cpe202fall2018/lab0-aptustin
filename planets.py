def weight_on_planets():
    # write your code here

    e_weight = input("What do you weigh on earth? ")

    # The following three lines casts the input as a float and converts the Earth weight to both Mars and Jupiter weight.
    e_weight = float(e_weight)

    m_weight = e_weight*.38

    j_weight = e_weight*2.34

    # Prints out the calculations performed above.
    print("\nOn Mars you would weigh", m_weight, "pounds.\nOn Jupiter you would weigh", j_weight,  "pounds.")


if __name__ == '__main__':
    weight_on_planets()
