from distutils.core import setup, Extension

spellfix1 = Extension('spellfix1',
                    sources = ['spellfix.c'])

setup (name = 'sqlite-spellfix',
       version = '1.0',
       description = 'Loadable spellfix1 extension for sqlite',
       py_modules = ['sqlite_spellfix'],
       ext_modules = [spellfix1])
