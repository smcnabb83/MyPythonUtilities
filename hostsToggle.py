import sys

sites = ["www.linkedin.com",
         "www.facebook.com",
         "twitter.com",
         "arstechnica.com",
         "news.ycombinator.com",
         "www.techdirt.com",
         "online-go.com",
         "xkcd.com",
         "www.amazon.com",
         "hackernoon.com",
         "mail.google.com",
         "www.codewars.com",
         "www.codingame.com",
         "www.quora.com",
         "calnewport.com",
         "www.myfitnesspal.com",
         "www.dotnetrocks.com",
         "tvtropes.org",
         "lichess.org",
         "brilliant.org",
         "www.reddit.com",
         "go4go.net",
         "knowyourmeme.com",
         "forbes.com",
         "ldjam.com",
         "itch.io",
         "calnewport.com",
         "zachtronics.com",
		 "reddit.com",
		 "chess.com",
		 "facebook.com",
		 "ycombinator.com",
		 "www.chess.com",
		 "www.facebook.com",
		 "www.ycombinator.com"]
		 
hostsFilePath = r'c:\windows\system32\drivers\etc\hosts'
newFileString = ""

with open(hostsFilePath) as hostsFile:
    line = hostsFile.readline()      
    while line:
        if(line[0] == "#"):
            newFileString += line
        line = hostsFile.readline()
    if(not(len(sys.argv) > 1 and sys.argv[1] == 'off')):
        for site in sites:
            newFileString += f'127.0.0.1\t{site}\n'

with open(hostsFilePath, 'w+') as writeHostsFile:
    writeHostsFile.write(newFileString)

    
