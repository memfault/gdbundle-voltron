# gdbundle-voltron

This is a [gdbundle](https://github.com/memfault/gdbundle) plugin for [snare/voltron](https://github.com/snare/voltron)

## Compatibility

This works for GDB, but it appears that the LLDB version of Voltron (as of [bcf25d957657414d025ff488889cdef8d4fcae06](https://github.com/snare/voltron/commit/bcf25d957657414d025ff488889cdef8d4fcae06)) does not work due not pinning versions in it's `setup.py` and does not work on Python 3.7. 

```
ImportError: cannot import name 'DispatcherMiddleware' from 'werkzeug.wsgi'
```

## Installation

After setting up [gdbundle](https://github.com/memfault/gdbundle), install the package from PyPi. 

```
$ pip install gdbundle-voltron
```

If you've decided to manually manage your packages using the `gdbundle(include=[])` argument,
add it to the list of plugins.

```
# .gdbinit

[...]
import gdbundle
plugins = ["voltron"]
gdbundle.init(include=plugins)
```

## Building

```
$ poetry build
$ poetry publish
```
