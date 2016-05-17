#!/usr/bin/env python

import hashlib
import sys
import base64

passed_string = sys.argv[1]

print "\n\t[+] Prints useful hashed / encoded values to help pentesters..\n"

print "MD5 Hash\t: %s  (%s Chars)" % (hashlib.md5((passed_string)).hexdigest(), len(hashlib.md5((passed_string)).hexdigest()))

print "SHA1 Hash\t: %s  (%s Chars)" % (hashlib.sha1((passed_string)).hexdigest(), len(hashlib.sha1((passed_string)).hexdigest()))

print "Sha224 Hash\t: %s  (%s Chars)" % (hashlib.sha224((passed_string)).hexdigest(), len(hashlib.sha224((passed_string)).hexdigest()))

print "SHA256 Hash\t: %s  (%s Chars)" % (hashlib.sha256((passed_string)).hexdigest(), len(hashlib.sha256((passed_string)).hexdigest()))

print "SHA384 Hash\t: %s  (%s Chars)" % (hashlib.sha384((passed_string)).hexdigest(), len(hashlib.sha384((passed_string)).hexdigest()))

print "Sha512 Hash\t: %s  (%s Chars)" % (hashlib.sha512((passed_string)).hexdigest(), len(hashlib.sha512((passed_string)).hexdigest()))

print "Base64\t\t: %s  (%s Chars)" % (base64.b64encode((passed_string)), len(base64.b64encode((passed_string))))


print "\n\t--------------Program Terminates-------------------\n"


