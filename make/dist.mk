.PHONY: dist publish coveralls

dist:                     ## Build source and built (wheel) distributions of the current version
	$(VENV_RUN); pip install --upgrade build twine; python -m build

publish: clean-dist dist  ## Publish the library to the central PyPi repository
	# make sure the dist archive contains a non-empty entry_points.txt file before uploading
	tar --wildcards --to-stdout -xf dist/localstack?core*.tar.gz "localstack?core*/localstack-core/localstack_core.egg-info/entry_points.txt" | grep . > /dev/null 2>&1 || (echo "Refusing upload, localstack-core dist does not contain entrypoints." && exit 1)
	$(VENV_RUN); twine upload dist/*

coveralls:                ## Publish coveralls metrics
	$(VENV_RUN); coveralls
