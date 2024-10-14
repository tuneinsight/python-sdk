"""
# Cryptography library

Computations on Tune Insight instances are performed encrypted, using the
[Lattigo](https://github.com/tuneinsight/lattigo) library for homomorphic encryption.
The `cryptolib` library implements Python bindings to interface with Lattigo, i.e.,
encrypting values and decrypting cyphertexts. This is mostly used for end-to-end
encrypted computations, where the result received by the client is a cyphertext.

This library is mostly intended for internal use.


## Troubleshooting

The `cryptolib` library interfaces with a compiled `.so`/`.dll` library that comes packaged with Diapason.
This library is loaded when the module is imported. If there is an error loading it, a warning will
be displayed. Most of the time, this warning can be safely ignored.

### _Could not load the cryptolib: contact your administrator._

This error occurs when trying to use the `cryptolib` but it wasn't loaded properly. Refer to the
warnings raised when importing `tuneinsight` to understand where the issue comes from (see below).

### _Could not find the cryptolib library. Your platform might not be supported._

The library was not compiled for your system and architecture. Please contact the Tune Insight team
to get a version compiled for your system.

Note that the Diapason comes pre-packaged with compiled libraries for most platforms. This error
might be caused by a path issue (check that the files are available in tuneinsight/cryptolib/build).

### _version `GLIBC_2.32' not found (required by /.../cryptolib-linux_x86_64.so)_

The `cryptolib` library requires [`glibc` 2.32](https://www.gnu.org/software/libc/) on Linux. Install
`glibc-2.32` on your system.

### _Failed to load cryptolib (`err`). Some functionality might be affected._

This depends on the error `err`. Contact the Tune Insight team for help.

"""

# Expose the cryptolib one level up (`from tuneinsight import cryptolib` should work)
from .cryptolib import *
