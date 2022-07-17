from typing import Dict


class InputManager(object):
    # Ask the user for an integer choice between 1 and upper limit, return the int
    @staticmethod
    def get_int_input(prompt, upper_limit):
        n = -1
        while(n < 1):
            response = input(prompt)
            try:
                if int(response) > 0 and int(response) <= upper_limit:
                    n = int(response)
                else:
                    raise ValueError("Invalid response")
            except ValueError:
                print(f"ERROR: please enter a number between 1 and {upper_limit}")
        return n

    # Ask the user for a floating point choice between 1 and upper_limit, return the float
    @staticmethod
    def get_float_input(prompt, upper_limit):
        if type(upper_limit) == str:
            upper_limit = float(upper_limit)

        n = -1
        while(n < 1):
            response = input(prompt)
            try:
                if float(response) > 0 and float(response) <= upper_limit:
                    n = float(response)
                else:
                    raise ValueError("Invalid response")
            except ValueError:
                print(f"ERROR: please enter a number between 1 and {upper_limit}")
        return round(n,2)

    # Ask the user to choose from the items in a list, or the items in a hash, return the list entry or hash key of their choice.
    @staticmethod
    def get_choice(choices, prompt="Please select an option: "):
        if isinstance(choices, dict):
            key_array = list(choices.keys())
            for i in range(0, len(key_array)):
                print(f'{i+1} {choices[key_array[i]]}')
            print("")
            n = InputManager.get_int_input(prompt,len(key_array))
            return(key_array[n - 1])
        else:
            for i in range(0, len(choices)):
                print(f'{i+1} {choices[i]}')
            print("")
            n = InputManager.get_int_input(prompt,len(choices))
            return(choices[n - 1])
