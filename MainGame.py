
if __name__ == '__main__':
    try:
        screen_cleaner()
        print(welcome("dolev"))
        load_game()
    except KeyboardInterrupt as e:
        print("\nBye Bye")
    except Exception as e:
        print(e)
