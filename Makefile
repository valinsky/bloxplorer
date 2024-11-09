gh-pages:
	git checkout gh-pages
	rm -rf _images _sources _static api
	git checkout main bloxplorer docs README.rst
	(cd docs && make html)
	mv -fv docs/_build/html/* ./
	rm -rf bloxplorer docs README.rst
	git add -A
	git commit -m "Generated gh-pages"
	git push
	git checkout main