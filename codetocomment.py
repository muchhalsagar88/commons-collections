import sys
import os

folder = None

if(len(sys.argv) > 1):
    folder = sys.argv[1]

codeFiles = []

if folder is not None:
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            if name.endswith('.java'):
                codeFiles += [root + '/' + name]


comment_count = 0
code_count = 0

for file in codeFiles:
    with open(file) as f:
        for line in f:
            line = line.strip()
            if len(line) is not 0:
                if (line.startswith('/**') or
                   line.startswith('*') or
                   line.startswith('//')):
                    comment_count += 1
                else:
                    code_count += 1

print "*****************************************************"
print "\t\tCUSTOM ANALYSIS"
print "*****************************************************"
print "Lines of Code:" + str(code_count)
print "Lines of Comments:" + str(comment_count)
code_to_comment_ratio = "{0:.2f}".format(float(code_count) / comment_count)
print "Code to Comment Ratio:" + code_to_comment_ratio
print "*****************************************************"
