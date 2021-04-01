#!/bin/bash

APPLICATIONS=("CyberHealth")

# shellcheck disable=SC1091
 source scripts/setup-postgres.sh 

for application in "${APPLICATIONS[@]}"
do
    (
        echo "Running in the folder $application"
        cd "$application" || exit
        # shellcheck disable=SC1091
        source scripts/start.sh 
    )
done