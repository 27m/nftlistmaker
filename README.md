# NFT List Maker

NFT List Maker is a very simple python script used to make NFT Lists for tradebots. (ex. OTB, Gear5 and Vector)

It is compatible with Windows and Linux. For any compatibility problems, open an issue.

It relies on the [Rolimon's Item API](https://www.rolimons.com/itemapi/itemdetails) to fetch details of every single limited item on the catalog. 

## What is a NFT list?

A NFT list tells your tradebot what items you don't want to send trades for / accept on. This is crucial for tradebotting so that you don't take losses and accept projected or fluctuating items.

## How to use:

First, you will need to install the requests and colorama modules.

Open a terminal and run ``pip install -r requirements.txt``

Then run the script either through Cmder or another terminal. 

## NOTE, Colorama [does not natively work](https://github.com/tartley/colorama/issues/103) on the Windows Terminal when using input() (which this script relies on). 
# You must install a terminal. [Cmder](https://cmder.net/) is recommended and has multiple benefits over Windows Terminal.

## This program is a work in progress!

Roadmap:

I plan to utilize a proxy and cache data from the Rolimon's API then fetch from this proxy through the program. 

This program will eventually auto-update / replace your tradebot config's previous NFT list.

## Discord 

marshall's basement (programs, minecraft services, etc) - https://discord.gg/BEXZdrVTDz

## Disclaimer

I am not responsible for your use of the Rolimon's API. This program should not be used to spam / abuse the API.

Thank you Rolimon for offering this API!

## Credits 

+ marshall#4949 - development
+ nicK#7461 - giving me details on rolimon's api
+ Egg#7087 - concept
+ Rolimon#0865 - API
+ 9ggy for a couple QOL improvements


