.PHONY: build serve clean deps

build:            ## generate _site/
	python3 build.py

serve: build      ## build and serve on http://localhost:8000
	cd _site && python3 -m http.server 8000

deps:             ## install the three build dependencies
	pip install -r requirements.txt

clean:
	rm -rf _site
