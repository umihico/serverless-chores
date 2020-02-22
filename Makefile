deploy:
	@make pytest
	sls deploy -v
	@make invoke
prod:
	@make pytest
	sls deploy -v --stage prod
	@make invoke
layer:
	rm -rf python && mkdir -p python
	docker run --rm -v $(shell pwd):/var/task -w /var/task lambci/lambda:build-python3.8 pip install ${package} -t ./python
	zip -r layer.zip python
	aws lambda publish-layer-version --layer-name ${package} --zip-file fileb://layer.zip --compatible-runtimes python3.8
	rm -rf layer.zip python
pytest:
	python3 -m py_compile *.py
	pytest *.py
invoke:
	sls invoke -f hourly
	sls invoke -f minutely
