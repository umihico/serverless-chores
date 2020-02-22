deploy:
	@make pytest
	sls deploy -v
	@make stage=dev invoke
prod:
	@make pytest
	sls deploy -v --stage prod
	@make stage=prod invoke
layer:
	# EXAMPLE: make package=requests ssm
	rm -rf python && mkdir -p python
	docker run --rm -v $(shell pwd):/var/task -w /var/task lambci/lambda:build-python3.8 pip install ${package} -t ./python
	zip -r layer.zip python
	aws lambda publish-layer-version --layer-name ${package} --zip-file fileb://layer.zip --compatible-runtimes python3.8 --compatible-runtimes python3.7 --profile umihico
	rm -rf layer.zip python
pytest:
	python3 -m py_compile *.py
	pytest *.py
invoke:
	sls invoke --stage ${stage} -f hourly
	sls invoke --stage ${stage} -f minutely
ssm:
	# EXAMPLE: make key=SLACK_TOKEN value=xoxp-00000000000000-abcdef ssm
	aws ssm put-parameter --name ${key} --type "String" --region ap-northeast-1 --overwrite --value ${value} --profile umihico
