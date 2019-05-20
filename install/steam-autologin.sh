#!/bin/bash

RESET=$(tput sgr0)
COLOR_RED=$(tput setaf 1)
BOLD=$(tput bold)

if ! [ -x "$(command -v steam)" ]; then
  echo ">> ${BOLD}${COLOR_RED}Error:${RESET} steam is not installed." >&2
  exit 1
fi

REGISTRY=$(echo "$HOME/.steam/registry.vdf")

if [ ! -f $REGISTRY ]
	then
		echo ">> ${BOLD}${COLOR_RED}Error:${RESET} Couldn't find $REGISTRY."
		exit 1
fi

if [ $# -eq 0 ]
	then
		echo ">> ${BOLD}${COLOR_RED}Error:${RESET} No username supplied. Please try again."
		exit 1
elif [ ${#1} -lt 4 ]
	then
		echo ">> ${BOLD}${COLOR_RED}Error:${RESET} Username too short. Please try again."
		exit 1
else
	USERNAME=$1
fi

sed -i "s/\"AutoLoginUser\"\t\t[^ ]*/\"AutoLoginUser\"\t\t\"${USERNAME}\"/" $REGISTRY

echo ">> Starting steam ..."
steam > /dev/null 2>&1 &
