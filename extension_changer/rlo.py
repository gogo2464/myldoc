import os
import sys
import shutil

new_extension = "txt"

# Reminder; mpSession.unicodeRtlo contains the extension we want to spoof, such as "jpg"
print(" [+] Inject %s false extension with unicode RTLO" % new_extension)
# Separate document path and extension

print(sys.argv[1])

(fileName, fileExtension) = os.path.splitext(sys.argv[1])


print("   [-] Extension %s " % fileExtension)
# Append unicode RTLO to file name
fileName += '\u202e' 
# Append extension to spoof in reverse order
fileName += '\ufeff' + new_extension[::-1] # Prepend invisible space so filename does not end with flagged extension
# Append file extension
fileName +=  fileExtension   
output_file = fileName
print("   [-] File name modified to: %s" %  output_file)

shutil.copy(sys.argv[1], output_file)