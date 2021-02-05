build:
	python3 -m build

upload:
	python3 -m twine upload dist/sqlite-spellfix-*.tar.gz

test-upload:
	python3 -m twine upload --repository testpypi dist/sqlite-spellfix-*.tar.gz
