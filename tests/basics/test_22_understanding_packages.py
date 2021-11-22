''' Understanding Packages '''
import sys

__author__ = 'Hari'

NOTES = '''
 Sometimes a collection of modules provides related functionality as part of a larger framework,
 then it makes sense to group all of them together. Packages allows you to group related modules together.

 The relationship between packages and modules is similar to that of directories and files in the
 filesystem. Packages can contain sub-packages and modules. In the filesystem a directory containing __init__.py
 is treated as a package when python tries to find packages on sys.path.

 A module with name a.b.c is saying that c is a module in package b which is a sub-package of module a.
'''

# from placeholders import *

# Look at the package1 and package2 directories before starting...

def test_package_basic_import():
    ''' testing package import '''
    clear_sys_modules()

    assert ("package1" in locals()) is False
    assert ("module1" in locals()) is False
    assert ("package1.module1" in locals()) is False

    import package1

    assert ("package1" in locals()) is True
    assert ("module1" in locals()) is False
    assert ("package1.module1" in locals()) is False

    assert type(package1).__name__ == 'module'

    assert ("package1" in sys.modules) is True
    assert ("module1" in sys.modules) is False
    assert ("package1.module1" in sys.modules) is False

    try:
        print(package1.module1.__doc__)
    except AttributeError :
        pass

    #modules need explicit import generally.
    import package1.module1
    print(package1.module1.__doc__)

    assert ("package1" in sys.modules) is True
    assert ("module1" in sys.modules) is False
    assert ("package1.module1" in sys.modules) is True


def clear_sys_modules():
    ''' clearing sys modules '''
    sys.modules.pop("module1", None)
    sys.modules.pop("package1", None)
    sys.modules.pop("package1.module1", None)
    sys.modules.pop("package1.subpackage", None)
    sys.modules.pop("package1.subpackage.m1", None)

def test_package_from_import():
    ''' testing package from import '''
    clear_sys_modules()

    assert ("package1" in locals()) is False
    assert ("module1" in locals()) is False
    assert ("package1.module1" in locals()) is False

    from package1 import module1

    assert ("package1" in locals()) is False
    assert ("module1" in locals()) is True
    assert ("package1.module1" in locals()) is False

    assert ("package1" in sys.modules) is True
    assert ("module1" in sys.modules) is False
    assert ("package1.module1" in sys.modules) is True


def test_package_import_failure():
    ''' testing package import failure '''
    clear_sys_modules()
    try:
        import package2
    except ImportError:
        # print(type(e))
        assert True

    # fill up reason for failure. why is package2 not a package
    why_it_failed = 'package2 does not have __init__.py'

def test_package_sub_packages():
    ''' testing subpackages from packages'''
    clear_sys_modules()

    assert ("package1" in locals()) is False
    assert ("subpackage" in locals()) is False
    assert ("package1.subpackage" in locals()) is False

    from package1 import subpackage

    assert ("package1" in locals()) is False
    assert ("subpackage" in locals()) is True
    assert ("package1.subpackage" in locals()) is False

    assert ("package1" in sys.modules) is True
    assert ("module1" in sys.modules) is False
    assert ("package1.module1" in sys.modules) is False
    assert ("package1.subpackage" in sys.modules) is True
    assert ("package1.subpackage.m1" in sys.modules) is True

    #why is this not raising an exception here?
    print(subpackage.m1.__doc__)

    assert ("package1.subpackage.m1" in sys.modules) is True

THREE_THINGS_I_LEARNT = """
- Importing Packages
- Modules in packages
- Subpackages
"""

TIME_TAKEN_MINUTES = 60
