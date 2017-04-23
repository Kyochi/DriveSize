import re
from drivesize.ApiDrive import ApiDrive
from drivesize.Tree import Tree

def main():

    api = ApiDrive()
    files = api.getFiles()
    if not files:
        print('No files found.')
    else:
        print('Total Files:')
        print(len(files))

    mydrive = Tree(api.root)
    mydrive.buildTree(files)
    print(mydrive.getSizeOf(mydrive.treesize))

    while True:
        regexStr = raw_input("Enter the name of the folder (regex) : ")
        print(regexStr)
        regex = re.compile(regexStr)
        for node in mydrive.folders:
            if (re.search(regex, node.m_name)):
                print(node.m_name+ " Size: " + str(node.m_size/pow(1024,3)) + " Go")

        print("")
    raw_input()

main()