""" Example python script utilizing basic arguments """

# The below are part of the python standard library
import argparse
import os


# Define function to parse arguments passed via the command line
def parse():
    """ Define function to parse arguments passed via the command line """
    parser = argparse.ArgumentParser(
        usage=f"{
            os.path.basename(__file__)
        } [-a1 'argument_1'] [-a2 'argument_2'] [-a3 'argument_3']",
        description="Commandline variables to streamline automation."
    )

    # Add argument 1
    parser.add_argument(
        "-a1",
        "--argument_1",
        dest="argument_1",
        action="store",
        type=str,
        required=False,
        help="The first argument of the script."
    )

    # Add argument 2
    parser.add_argument(
        "-a2",
        "--argument_2",
        dest="argument_2",
        action="store",
        type=str,
        required=False,
        help="The second argument of the script."
    )

    # Add argument 3
    parser.add_argument(
        "-a3",
        "--argument_3",
        dest="argument_3",
        action="store",
        type=str,
        required=False,
        help="The third argument of the script."
    )

    return parser.parse_args()


# Beginning of main
if __name__ == "__main__":
    # Get command line arguments
    args = parse()

    # Check arguments, and if they aren't passed, ask user for them
    # Create a list of argument keys
    argument_keys = vars(args).keys()

    # For each of the arguments, check to see if they are equal to None.
    # If equal to none, prompt user to input a value
    for key in argument_keys:
        if getattr(args, key) is None:
            if key == "argument_1":
                args.argument_1 = input(
                    "Please enter the first argument for the script: "
                )
            if key == "argument_2":
                args.argument_2 = input(
                    "Please enter the second argument for the script: "
                )
            if key == "argument_3":
                args.argument_3 = input(
                    "Please enter the third argument for the script: "
                )

    # Print out the passed arguments
    print(f"Here is argument 1: {args.argument_1}")
    print(f"Here is argument 2: {args.argument_2}")
    print(f"Here is argument 3: {args.argument_3}")
