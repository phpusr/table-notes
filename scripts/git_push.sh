#!/usr/bin/env bash

git_tag() {
    git checkout develop && git tag $1 && git push --tags && \
        git_push
}

git_push() {
    git checkout develop && git push && \
        git checkout master && git merge develop && git push && \
        git checkout develop
}

if [[ $1 == '' ]]; then
    git_push
else
    git_tag $1
fi
