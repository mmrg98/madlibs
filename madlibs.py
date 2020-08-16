def main():
        time=input("choose time from 1-12: ")
        items=input("enter any items: ")
        name=input("enter any name: ")
        scream=input("enter screaming phase: ")
        action=input("enter any action: ")
        print(""" It was %s o\'clock when I heard a knock at the door.
I opened the door and there was a box full of %s with a note saying \"From Mr. %s \"
Just as I closed the door I heard a scream \"%s.\"
I froze in place and all I could do was %s.""" % (time, items, name.title(), scream.upper(), action))


if __name__ == '__main__':
	main()
