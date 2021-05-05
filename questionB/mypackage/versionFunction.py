def versionChecker( a, b):
        #remove '.' from each string parameters before conditional checking
        aTemp= str(a).replace('.', '')
        bTemp=str(b).replace('.', '')

        if (aTemp==bTemp):
            answer = "{} version is equal to version {}".format(a, b)
            result=answer
        else:
            print('the two versions are not equal')
            if (aTemp<bTemp):
                answer = "{} version is smaller than version {}".format(a, b)
                result=answer

            else:
                answer = "{} version is larger than version {}".format(a, b)
                result=answer
        return result