__author__ = 'Hari'

notes = '''
 Sometimes a collection of modules provides related functionality as part of a larger framework,
 then it makes sense to group all of them together. Packages allows you to group related modules together.
 The relationship between packages and modules is similar to that of directories and files in the
 filesystem. Packages can contain sub-packages and modules. In the filesystem a directory containing __init__.py
 is treated as a package when python tries to find packages on sys.path.
 A module with name a.b.c is saying that c is a module in package b which is a sub-package of module a.
'''

#from placeholders import *
import sys

from package import module1
# Look at the package1 and package2 directories before starting...

def test_package_basic_import():
    clear_sys_modules()

    assert False == ("package" in locals())
    assert False == ("module1" in locals())
    assert False == ("package.module1" in locals())

    import package

    assert True == ("package" in locals())
    assert False == ("module1" in locals())
    assert False == ("package.module1" in locals())

    assert "module" == type(package).__name__

    assert True == ("package" in sys.modules)
    assert False == ("module1" in sys.modules)
    assert False == ("package.module1" in sys.modules)

    try:
        print (package.module1.__doc__)
    except AttributeError :
        pass

    #modules need explicit import generally.
    import package.module1
    print (package.module1.__doc__)

    assert True == ("package" in sys.modules)
    assert False == ("module1" in sys.modules)
    assert True == ("package.module1" in sys.modules)


def clear_sys_modules():
    sys.modules.pop("module1", None)
    sys.modules.pop("package", None)
    sys.modules.pop("package.module1", None)
    sys.modules.pop("package.subpackage", None)
    sys.modules.pop("package.subpackage.m1", None)

def test_package_from_import():
    clear_sys_modules()

    assert False == ("package" in locals())
    assert False == ("module1" in locals())
    assert  False == ("package.module1" in locals())

    from package import module1

    assert False == ("package" in locals())
    assert True == ("module1" in locals())
    assert False == ("package.module1" in locals())

    assert True == ("package" in sys.modules)
    assert False == ("module1" in sys.modules)
    assert True == ("package.module1" in sys.modules)


def test_package_import_failure():
    clear_sys_modules()
    try:
        import package_2
    except ImportError  :
        assert True

    # fill up reason for failure. why is package2 not a package
   # why_it_failed = Because every package must have __init__ method

def test_package_sub_packages():
    clear_sys_modules()

    assert False == ("package" in locals())
    assert False == ("subpackage" in locals())
    assert False == ("package.subpackage" in locals())

    from package import subpackage

    assert False == ("package" in locals())
    assert True == ("subpackage" in locals())
    assert False == ("package.subpackage" in locals())

    assert True == ("package" in sys.modules)
    assert False == ("module1" in sys.modules)
    assert False == ("package.module1" in sys.modules)
    assert True == ("package.subpackage" in sys.modules)
    assert False == ("package.subpackage.m1" in sys.modules)

    #why is this not raising an exception here?
    # TODO: Fixed the import statement
    try:
        from package.subpackage import m1
        print(subpackage.m1.__doc__)
    except NameError as e:
        print(e)
    

    assert True == ("package.subpackage.m1" in sys.modules)

three_things_i_learnt = """
- packages and subpackages
- Handling Errors while importing
- Try except block
"""

#time_taken_minutes = '30 min'