def validate_user_input(prompt: str, valid_inputs: list[str],
                        error_message: str = "Invalid input. Please try again.") -> str:
    """Get user input and validate against a list of valid options."""
    while True:
        u_input = input(prompt)
        u_input = u_input.lower()
        valid_inputs = [i.lower() for i in valid_inputs]

        if u_input in valid_inputs:
            return u_input
        print(error_message)


def get_login_screen_decision():
    return validate_user_input(
        "Type in your option: ",
        ["1", "2", "q"]
    )