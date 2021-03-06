#!/usr/bin/env bash

remote_dir='${HOME}/robot_fridge'
branch=${1:-dev}
remote_host="pi"

echo "Running on ${remote_host}: 'cd ${remote_dir}; git pull; git checkout dev'"
ssh "${remote_host}" "cd ${remote_dir}; git pull; git checkout ${branch}"
