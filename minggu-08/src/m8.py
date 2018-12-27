import sys, warnings
if sys.version_info.major < 3:
    warnings.warn("Butuh Python 3.0 untuk menjalankan program ini",
        RuntimeWarning)
else:
    print('Program dijalankan secara normal')