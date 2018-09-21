def weight_on_planets():
   # write your code here

   e_weight = input("What is your weight on earth?")

   e_weight = float(e_weight)

   m_weight = e_weight*.38

   j_weight = e_weight*2.34

print "\nOn Mars you would weigh " + m_weight + " pounds.\nOn Jupiter you would weigh " + j_weight + " pounds."


if __name__ == '__main__':
   weight_on_planets()