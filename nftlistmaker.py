from cmd import Cmd
from requests import get
from colorama import Fore, Style, init

# Resets the color of the message after every message sent.
init(autoreset=True)


class NFTMaker(Cmd):
    def do_make(self, arg):
        """Starts the process of making an NFT list."""
        items, nftlist = get('https://www.rolimons.com/itemapi/itemdetails').json()['items'], []

        x = input(Fore.GREEN + "All projecteds? (recommended) | Y or N ")
        if x.lower() == "y":
            for item in items:
                if items[item][7] == 1:
                    nftlist.append(item)

        x = input(Fore.LIGHTYELLOW_EX + "\nAll unvalued (RAP) items? | Y or N: ")
        if x.lower() == "y":
            for item in items:
                if items[item][3] == -1:
                    if str(item) in nftlist:
                        pass
                    else:
                        nftlist.append(item)

        x = input(Fore.LIGHTMAGENTA_EX + "\nAll Gucci items? | Y or N: ")
        if x.lower() == "y":
            for item in items:
                if "gucci" in items[item][0].lower():
                    if str(item) in nftlist:
                        pass
                    else:
                        nftlist.append(item)

        x = input(Fore.BLUE + "\nAll Ralph Lauren items? -- Y or N: ")
        if x.lower() == "y":
            for item in items:
                if "ralph lauren" in items[item][0].lowerl
                    if str(item) in nftlist:
                        pass
                    else:
                        nftlist.append(item)

        with open("nftlist.txt", "w") as nftfile:
            nftfile.write(", ".join(nftlist))

        print(
            Style.BRIGHT + Fore.WHITE + "\nFinished creating your NFT list, check the directory that the script is in.")
        return

    def do_quit(self, arg):
        """Quits the program."""

        print("Quitting.")
        raise SystemExit

    def do_discord(self, arg):
        """Prints the discord invite link."""

        print("https://discord.gg/ERUYUCZfWJ")
        return

    def do_credits(self, arg):
        """Displays the credits for this program."""

        print("marshall#4949 - development \nnicK#7461 - giving me details on rolimon's api \nEgg#7087 - concept")
        return


if __name__ == '__main__':
    prompt = NFTMaker()
    prompt.prompt = Fore.LIGHTBLUE_EX + '> '
    prompt.cmdloop('Enter "help" for a list of commands.')
