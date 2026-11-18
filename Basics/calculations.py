# Learning how to use *args

def get_maximum(*args):
    if not args:
        return None

    max_number = args[0]

    for number in args[1:]:
            
        if number > max_number:
            max_number = number
    return max_number

if __name__ == "__main__":
    print("Testing text")
