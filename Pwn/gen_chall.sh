set -ueo pipefail
name="${1:?Challenge name not given!}"

cp -R Template/ "$1"
cd "$1"
# Change stuff here
mv README.md pwn-template-info.md
cp ../../README-template.md README.md
