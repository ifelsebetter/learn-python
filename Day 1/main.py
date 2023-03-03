# Import modules / files
import boolean
import operator
import type_of_number
import variable
import get_input
import arrays

# Call function from import modules / files

def main():

    print("Boolean")
    boolean.true_false()
    
    print("\nOperator")
    operator.normal_operator()
    operator.assign_operator()
    operator.relational_operator()
    
    print("\nTypes of number")
    type_of_number.types_of_number()

    print("\nVariable")
    variable.assign_display_var()
    
    print("\nInput")
    get_input.get_user_input()

    print("\nArray")

    arrays.list()


main()
