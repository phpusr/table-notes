#!/usr/bin/env bash

push() {
    git checkout develop && git tag $1 && git push && git push --tags && \
        git checkout master && git merge develop && git push && \
        git checkout develop
}

if [[ $1 == '' ]]; then
    echo 'usage: ./git_push <tag>'
else
    push $1
fi
