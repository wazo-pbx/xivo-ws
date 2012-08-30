.PHONY: build
build:
	python setup.py sdist -f

.PHONY: upload
upload: build
	python setup.py register upload

.PHONY: clean
clean:
	rm -rf MANIFEST build dist
