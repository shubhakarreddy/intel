import getopt, sys
import war

def parse_args():
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hv", ["help", "verbose"])
    except getopt.GetoptError:
        print("Invalid options!")
        usage()
        sys.exit()

    return opts

def usage():
    print("\nCommand to run\n \
            Usage: "+sys.argv[0]+" [option(s)]\n \
            Options:\n \
            -h or --help: Display the command to run and options\n \
            -v or --verbose: Show verbose output of the game\n")

if __name__ == "__main__":
    opts = parse_args()
    verbose = False

    for opt, args in opts:
        if opt in ("-v", "--verbose"):
            verbose = True


        if opt in ("-h", "--help"):
            usage()
            sys.exit()

    game = war.War(verbose_output=verbose)
    print(game.run())

    while True:
        answer = input("Play another around?[y/n]:")
        if answer == 'y' or answer == 'Y':
            game = war.War(verbose_output=verbose)
            print(game.run())
        elif answer == 'n' or answer == 'N':
            break
        else:
            "Enter valid input!!"
