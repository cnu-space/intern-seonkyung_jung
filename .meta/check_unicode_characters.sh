#!/bin/bash

# https://gist.github.com/aigjermo/753665d5317a87341091
#
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.

# def comparison target
if git rev-parse --verify HEAD >/dev/null 2>&1
then
    against=HEAD
else
    # Initial commit: diff against an empty tree object
    against=4b825dc642cb6eb9a060e54bf8d69288fbee4904
fi

# Redirect output to stderr.
exec 1>&2

# Abort a commit if you have non ASCII characters in
# the commit, and output the non ASCII characters.
#echo "Checking for unicode characters and trailing whitespace"

chars="$(git diff --unified=0 "${against}" | grep -e "^+" | tr -d "\000-\011\013-\177" | tr -d '\n')"
cnt="${#chars}"
if [ -n "${chars}" ]; then
    echo "Error: Non ascii characters found in change set:"
    for ((i=0; i < cnt; i++))
    do
        char="${chars:$i:1}"
        echo ""
        echo "Found character '${char}':"
        git --no-pager diff HEAD -S"${char}"
    done
    exit 1
fi

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.

# Note that the use of brackets around a tr range is ok here, (it's
# even required, for portability to Solaris 10's /usr/bin/tr), since
# the square bracket bytes happen to fall in the designated range.
yesno=$(git diff --cached --name-only --diff-filter=A -z "${against}" | LC_ALL=C tr -d '[ -~]\0' | wc -c)
if test ${yesno} != 0
then
    echo "Error: Attempt to add a non-ASCII file name."
    exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
#exec git diff-index --check --cached $against --
