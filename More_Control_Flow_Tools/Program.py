import if_Statements
import for_Statements
import The_range_Function
import break_and_continue_Statements_and_else_Clauses_on_Loops
import match_Statements
import Defining_Functions
import Default_Argument_Values
import Keyword_Arguments
import Special_parameters
import Unpacking_Argument_Lists
import Lambda_Expressions
import Documentation_Strings
import Function_Annotations


selection = "-1"
while selection != "0":
    print("----------------------------Menu----------------------------")
    print("1. if_Statements")
    print("2. for_Statements")
    print("3. The_range_Function")
    print("4. break_and_continue_Statements_and_else_Clauses_on_Loops")
    print("5. match_Statements")
    print("6. Defining_Functions")
    print("7. Default_Argument_Values")
    print("8. Keyword _Arguments")
    print("9. Special_parameters")
    print("10. Unpacking_Argument_Lists")
    print("11. Lambda_Expressions")
    print("12. Documentation_Strings")
    print("13. Function_Annotations")
    print("0. Exit")
    print("----------------------------Menu----------------------------")
    selection = input("Enter selection: ")
    if selection == "1":
        if_Statements.Demo()
    elif selection == "2":
        for_Statements.Demo()
    elif selection == "3":
        The_range_Function.Demo()
    elif selection == "4":
        break_and_continue_Statements_and_else_Clauses_on_Loops.Demo()
    elif selection == "5":
        match_Statements.Demo()
    elif selection == "6":
        Defining_Functions.Demo()
    elif selection == "7":
        Default_Argument_Values.Demo()
    elif selection == "8":
        Keyword_Arguments.Demo()
    elif selection == "9":
        Special_parameters.Demo()
    elif selection == "10":
        Unpacking_Argument_Lists.Demo()
    elif selection == "11":
        Lambda_Expressions.Demo()
    elif selection == "12":
        Documentation_Strings.Demo()
    elif selection == "13":
        Function_Annotations.Demo()
    elif selection == "0":
        exit()
    else:
        print("Again")
