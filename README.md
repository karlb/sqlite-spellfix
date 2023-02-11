# sqlite-spellfix

This python package includes a loadable `spellfix1` extension module for sqlite. This allows other python packages to use this extension without requiring dependencies outside of the python ecosystem. For more details on the extension itself, see [the official documentation](https://www.sqlite.org/spellfix1.html).

## Installation

### Latest Release

Install the `sqlite-spellfix` package from pypi.

### Current Development Version

Install via pip

```sh
pip install git+https://github.com/karlb/sqlite-spellfix
```

or add this to you requirements.txt:

```
git+https://github.com/karlb/sqlite-spellfix
```


## Usage


```python
import sqlite3
import sqlite_spellfix

conn = sqlite3.connect(":memory:")
conn.enable_load_extension(True)
conn.load_extension(sqlite_spellfix.extension_path())
# now use as described in https://www.sqlite.org/spellfix1.html
```

## See Also
* [sqlite-icu python package](https://github.com/karlb/sqlite-icu)
