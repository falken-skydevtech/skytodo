#!/bin/bash

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done

DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
NOW="$(date +'%Y%m%d-%H%M%S')"

cd "$DIR/../.."

rsync -avz skytodo skydevtech.mockup:~/
ssh skydevtech.mockup 'chmod +x ~/skytodo/__scripts__/*.sh'
ssh skydevtech.mockup './skytodo/__scripts__/update-config-to-ovh.sh'
