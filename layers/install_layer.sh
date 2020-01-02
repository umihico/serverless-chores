#!/bin/sh

# EXAMPLE: sh install_layer.sh requests

export PACKAGE_NAME=$1
export OUTPUT_DIR="python"

rm -rf ${PACKAGE_NAME} && mkdir -p ${PACKAGE_NAME}/${OUTPUT_DIR}
docker run --rm -v $(pwd):/var/task -w /var/task lambci/lambda:build-python3.8 pip install ${PACKAGE_NAME} -t ${PACKAGE_NAME}/${OUTPUT_DIR}
