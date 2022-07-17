from typing import Dict


class InputManager(object):
    @staticmethod
    def get_numeric_input(prompt, upper_limit):
        n = - 1
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

    @staticmethod
    def get_choice(choices, prompt="Please select an option: "):
        if isinstance(choices, dict):
            key_array = list(choices.keys())
            for i in range(0, len(key_array)):
                print(f'{i+1} {choices[key_array[i]]}')
            print("")
            n = InputManager.get_numeric_input(prompt,len(key_array))
            return(key_array[n - 1])
        else:
            for i in range(0, len(choices)):
                print(f'{i+1} {choices[i]}')
            print("")
            n = InputManager.get_numeric_input(prompt,len(choices))
            return(choices[n - 1])