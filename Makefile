deploy:
	sls deploy -v
prod:
	sls deploy -v --stage prod
layer:
	rm -rf python && mkdir -p python
	docker run --rm -v $(shell pwd):/var/task -w /var/task lambci/lambda:build-python3.8 pip install ${package} -t ./python
	zip -r layer.zip python
	aws lambda publish-layer-version --layer-name ${package} --zip-file fileb://layer.zip --compatible-runtimes python3.8
	rm -rf layer.zip python
