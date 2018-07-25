#!/usr/bin/env python
import argparse
import os
import subprocess

# Define the command-line arguments
parser = argparse.ArgumentParser(description='AS115 1.0 (wrapper for AS31) -- Report AS115 problems to trehans@mit.edu and AS31 problems to paul@pjrc.com')
parser.add_argument('filename', metavar='file.asm', type=str, help='file to assemble')
parser.add_argument('-l', '--list', help='create list file', action='store_true')
parser.add_argument('-s', '--stdout', help='send output to stdout', action='store_true')
parser.add_argument('-F', '--Format', choices=['hex', 'bin', 'tdr', 'byte', 'od', 'srec2', 'srec3', 'srec4'], help='output format (intel hex default)', default='hex')
parser.add_argument('-A', '--Another', choices=['hex', 'bin', 'tdr', 'byte', 'od', 'srec2', 'srec3', 'srec4'], help='optional output format argument', default=None)

# Parse the command-line arguments
args = parser.parse_args()

# Change the current working directory into the directory that contains our main file
fullpath = os.path.abspath(args.filename)
filename = os.path.basename(fullpath)
dirname = os.path.dirname(fullpath)
os.chdir(dirname)

# Construct the larger assembly file from the smaller assembly files by looking for .inc directives
stack = [('.inc', filename)]
allContents = []
while (len(stack) > 0):
    (t, s) = stack.pop()
    if t == '.inc':
        with open(s, 'r') as f:
            for line in f:
                line = line.rstrip()
                if line.startswith('.inc'):
                    incfile = line[5:]
                    stack.append(('line', '; ==== Included from \"' + incfile + '\" by AS115: ===='))
                    stack.append(('.inc', incfile))
                else:
                    stack.append(('line', line))
    else:
        allContents.append(s)

allContents.reverse()
compiledFile = '\n'.join(allContents) + '\n'

# Save the file
outputFilename = filename.replace('.asm', '.out.asm')
with open(outputFilename, 'w') as f:
    f.write(compiledFile)

# Compile a list of arguments for AS31
as31args = ['as31']
if args.list:
    as31args.append('-l')
if args.stdout:
    as31args.append('-s')
if args.Another is not None:
    as31args.append('-A' + args.Another)
as31args.append('-F' + args.Format)
as31args.append(outputFilename)

# Run AS31 on the resulting asm file
subprocess.call(as31args)
