IVERSION = (0, 1)
VERSION = ".".join(str(i) for i in IVERSION)
MINORVERSION = ".".join(str(i) for i in IVERSION[:2])
NAME = "astgen"
NAMEVERSION = NAME + " " + VERSION