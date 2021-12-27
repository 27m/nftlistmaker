from cmd import Cmd
import requests

response = requests.get('https://www.rolimons.com/itemapi/itemdetails')
items = response.json()['items']


class NFTMaker(Cmd):
    def do_make(self, arg):
        """Starts the process of making an NFT list."""

        nftlist = []

        x = input("All projecteds? (recommended) -- y or n ")
        if x.lower() == "y":
            for item in items:
                if items[item][7] == 1:
                    nftlist.append(item)

        x = input("\nAll unvalued (RAP) items? -- y or n ")
        if x.lower() == "y":
            for item in items:
                if items[item][3] == -1:
                    if str(item) in nftlist:
                        pass
                    else:
                        nftlist.append(item)

        x = input("\nAll Gucci items? -- y or n ")
        if x.lower() == "y":
            for item in items:
                if "gucci" in items[item][0].lower():
                    if str(item) in nftlist:
                        pass
                    else:
                        nftlist.append(item)

        x = input("\nAll Ralph Lauren items? -- y or n ")
        if x.lower() == "y":
            for item in items:
                if "ralph lauren" in items[item][0].lower():
                    if str(item) in nftlist:
                        pass
                    else:
                        nftlist.append(item)
        file = open("nftlist.txt", "w")
        file.write(", ".join(nftlist))

    def do_quit(self, arg):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit

    def do_discord(self, arg):
        """Prints the discord invite link."""
        print("https://discord.gg/ERUYUCZfWJ")

    def do_credits(self, arg):
        """Displays the credits for this program."""
        print("marshall#4949 - development \nnicK#7461 - giving me details on rolimon's api \nEgg#7087 - concept")


if __name__ == '__main__':
    prompt = NFTMaker()
    prompt.prompt = '> '
    prompt.cmdloop('Enter "help" for a list of commands.')
