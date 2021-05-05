def versionChecker( a, b):
        #remove '.' from each string parameters before conditional checking
        aTemp= str(a).replace('.', '')
        bTemp=str(b).replace('.', '')

        if (aTemp==bTemp):
            print(a,'version is equal to version',b)
            result="equal"
        else:
            print('the two versions are not equal')
            if (aTemp<bTemp):
                print(a,'version is smaller than version',b)
                result="smaller"

            else:
                print(a,'version is larger than version',b)
                result="greater"
        return result