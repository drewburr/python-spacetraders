#!/bin/sh
# Generate a client from current API spec

CLONE_DIR='./api-docs'

poetry install --only dev

if [ -d $CLONE_DIR ]
then
    echo "Pulling updates from SpaceTradersAPI/api-docs"
    cd $CLONE_DIR
    git fetch
    git pull
    cd -
else
    echo "Cloning SpaceTradersAPI/api-docs"
    git clone https://github.com/SpaceTradersAPI/api-docs $CLONE_DIR
fi

cd $CLONE_DIR
npx @redocly/cli@latest bundle --lint-config error -o ../bundle.json
cd -

poetry run openapi-python-client update \
    --path bundle.json \
    --meta none \
    --config openapi-client.yml \
    --custom-template-path=openapi-client-template
