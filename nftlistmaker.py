from cmd import Cmd
import logging
import time
from requests import get
from colorama import Fore, Style, init

logging.basicConfig(filename='logs.txt', filemode='a', level=logging.DEBUG, format='[%(levelname)s] - {%(asctime)s} %(message)s')

# Resets the color of the message after every message sent.
init(autoreset=True)


class NFTMaker(Cmd):
    def do_make(self, arg):
        """Starts the process of making an NFT list."""

        start1 = time.perf_counter()
        items, nftlist = get('https://m2rsh.xyz/roli').json()['items'], []
        end1 = time.perf_counter()
        x = input("\n" + Style.BRIGHT + Fore.GREEN + "All projecteds? (recommended) | Y or N ")
        if x.lower() == "y":
            for item in items:
                if items[item][7] == 1:
                    nftlist.append(item)

        x = input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "\nAll unvalued (RAP) items? (CAUTION: This is a lot of items) | Y or N: ")
        if x.lower() == "y":
            for item in items:
                if items[item][3] == -1:
                    if str(item) in nftlist:
                        pass
                    else:
                        nftlist.append(item)

        x = input(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "\nAll Gucci items? | Y or N: ")
        if x.lower() == "y":
            for item in items:
                if "gucci" in items[item][0].lower():
                    if str(item) in nftlist:
                        pass
                    else:
                        nftlist.append(item)

        x = input(Style.BRIGHT + Fore.BLUE + "\nAll Ralph Lauren items? -- Y or N: ")
        if x.lower() == "y":
            for item in items:
                if "ralph lauren" in items[item][0].lower():
                    if str(item) in nftlist:
                        pass
                    else:
                        nftlist.append(item)
        start2 = time.perf_counter()
        with open("nftlist.txt", "w") as nftfile:
            nftfile.write(", ".join(nftlist))
        end2 = time.perf_counter()

        print(Style.BRIGHT + Fore.WHITE + "\nFinished creating your NFT list, check the directory that the script is in.")
        logging.debug(f"Proxy fetch elapsed time {str(end1 - start1)[0:5]}s | List write elapsed time {str(end2 - start2)[0:6]}s.")
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
