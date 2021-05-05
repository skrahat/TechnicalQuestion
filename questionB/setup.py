from setuptools import setup, find_packages

VERSION = '1.0' 
DESCRIPTION = 'Technical question 2 module'
LONG_DESCRIPTION = 'version checker'

# Setting up
setup(
       
        name="versionCheckModule", 
        version=VERSION,
        author="asaduzzaman rahat",
        author_email="<asaduzzaman.rahat@mail.mcgill.ca>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)