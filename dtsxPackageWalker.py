from os import walk, path
import argparse
from datetime import datetime


class arguments:
    startpaths = []
    extensions = []
    filename = ""
    silent = False
    getCreationDate = False
    separator = ","


def getFileLogString(root, file, args):
    filepath = path.join(root, file)
    fileCreationTime = ""
    if(args.getCreationDate):
        fileCreationTime = args.separator
        fileTimeSeconds = path.getmtime(filepath)
        fileTime = datetime.fromtimestamp(fileTimeSeconds)
        fileCreationTime += fileTime.strftime('%m/%d/%Y')
    return filepath + fileCreationTime


def findFileWalk(args):
    with open(args.filename, "w+") as ssisFiles:
        for loc in args.startpaths:
            for root, dirs, files in walk(loc):
                for file in files:
                    for ext in args.extensions:
                        if file.endswith(ext):
                            logText = getFileLogString(root, file,
                                                       args)
                            if(not args.silent):
                                print(logText)
                            ssisFiles.write(logText)


def parseArguments():
    parser = argparse.ArgumentParser()

    pathsHelp = """pass a semicolon-separated list of paths
    that you want to search for"""
    parser.add_argument("paths", help=pathsHelp)

    extensionsHelp = """pass a semicolon-separated list of
    extensions that you want to search for"""
    parser.add_argument("extensions", help=extensionsHelp)

    filenameHelp = """pass a file that you want to write the
    results to. Defaults to files.txt"""
    parser.add_argument("-filename", default="files.txt",
                        help=filenameHelp)

    silentHelp = """pass the silent flag if you do not want
    the program to print every match to the screen"""
    parser.add_argument("-si", "-silent", action="store_true",
                        help=silentHelp)

    fileTimeHelp = """pass the fileModifiedTime (fm) flag to
    have the file creation time appended to every entry
    in the output list"""
    parser.add_argument("-fm", "-filemodifiedtime",
                        action="store_true",
                        help=fileTimeHelp)

    separatorHelp = """pass the separator you want to use
    between the file name and file creation date
    (default is ",")"""
    parser.add_argument("-sp", "-separator", default=",",
                        help=separatorHelp)

    args = parser.parse_args()
    pargs = arguments()

    pargs.startpaths = args.paths.split(";")
    pargs.extensions = args.extensions.split(";")
    pargs.filename = args.filename
    pargs.silent = args.si
    pargs.getCreationDate = args.fm
    pargs.separator = args.sp

    return pargs


def prog():
    args = parseArguments()
    findFileWalk(args)


if __name__ == "__main__":
    prog()
