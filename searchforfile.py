import os
import re
import argparse

programmingFileTypes = re.compile(r"\.(accdb|accde)$", re.IGNORECASE)
# Fill this out with network locations you want to search
programmingFileLocations = [r"\\elite\facstaff$"]


class programArgs:
    updateFileLocationList = False
    overwriteFileLocationList = False
    searchString = ""
    fileListFileName = r"c:\scripts\filelist.txt"


class screen:
    def __init__(self):
        self.curSearch = ""
        self.count = 0
        self.filesFound = []

    def incrementCount(self):
        self.count += 1
        self._refreshScreen()

    def appendFoundFile(self, file):
        self.filesFound.append(file)
        self._refreshScreen()

    def updateCurSearch(self, path):
        self.curSearch = path
        self._refreshScreen()

    def __str__(self):
        strret = f"searching {self.curSearch}, found:\n"
        strret += '\n'.join(self.filesFound)
        return strret

    def _refreshScreen(self):
        os.system('cls')
        scrString = f"searching {self.curSearch}, found:\n"
        scrString += '\n'.join(self.filesFound)
        scrString += '\n'.join(self.filesFound)
        print(scrString)


def walker(path, searchstring, scr):
    for root, dirs, files in os.walk(path):
        scr.updateCurSearch(root)
        for file_ in files:
            if programmingFileTypes.search(str(file_)):
                scr
                try:
                    openfile = open(os.path.join(root, file_))
                    if searchstring.lower() in openfile.read().lower():
                        scr.appendFoundFile(os.path.join(root, file_))
                except:
                    scr.appendFoundFile(f'file {file_} unreadable, skipping')
                finally:
                    openfile.close()


def findFilePaths(path, args):
    outlist = []
    for root, dirs, files in os.walk(path):
        for file_ in files:
            if programmingFileTypes.search(str(file_)):
                if root not in outlist:
                    outlist.append(root)

    if os.path.exists(r'c:\scripts\filelist.txt'):
        append_write = 'w+'
    else:
        append_write = 'w+'

    with open(r"c:\scripts\fileList.txt", append_write) as myFile:
        myFile.write(','+','.join(outlist))


def processArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("search_string")
    parser.add_argument("-file_location_list",
                        default=r"c:\scripts\filelist.txt")
    UpdateHelp = "set if you want to update a file\
            location list instead of search for a string"
    parser.add_argument("-uf", "-update-files", action="store_true",
                        help=UpdateHelp)
    parser.add_argument("-nf", "-newfile", action="store_true")

    args = parser.parse_args()
    pargs = programArgs()

    pargs.searchString = args.search_string
    pargs.fileListFileName = args.file_location_list
    pargs.updateFileLocationList = args.uf
    pargs.overwriteFileLocationList = args.nf

    return pargs


def mainApp():
    scr = screen()
    PathsList = []

    args = processArguments()

    if(not args.updateFileLocationList):
        with open(args.fileListFileName) as fileslist:
            for line in fileslist:
                currentLine = line.split(",")
                for cl in currentLine:
                    PathsList.append(cl)
    else:
        PathsList = programmingFileLocations

    for location in PathsList:
        if(args.updateFileLocationList):
            findFilePaths(location, args)
        else:
            walker(location, args.searchString, scr)


mainApp()
