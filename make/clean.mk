.PHONY: clean clean-dist

clean:                    ## Clean up (npm dependencies, downloaded infrastructure code, compiled Java classes)
	rm -rf .filesystem
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf localstack-core/*.egg-info
	rm -rf $(VENV_DIR)

clean-dist:               ## Clean up python distribution directories
	rm -rf dist/ build/
	rm -rf localstack-core/*.egg-info
