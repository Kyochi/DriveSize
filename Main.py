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

main()