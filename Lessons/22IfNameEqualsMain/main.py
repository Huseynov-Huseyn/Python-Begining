# if __name__ == '__main__':
#   - Used to check if this script is being run directly or imported as a module.
#   - When run directly: Python sets __name__ = '__main__' (code inside this block executes).
#   - When imported: Python sets __name__ to the file name (code inside this block is ignored).
#
# Benefits:
#   - Makes code modular and reusable.
#   - Prevents code from running automatically when imported into other files.
#   - Better code structure and readability.


def main():
    print("This is the main class")

if __name__=='__main__':
    main()