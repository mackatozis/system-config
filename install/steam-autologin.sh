#!/bin/bash

# This script enables you to switch between steam accounts
# without the need to enter credential and a Steam Guard 
# code everytime.
#
# Usage: $ bash steam-autologin USERNAME
# Note: You will need to put your credentials and check
# the box 'Remember Me' the first time you run the script.

# Steam registry location
REGISTRY=$(echo "$HOME/.steam/registry.vdf")
# Custom colors
RESET=$(tput sgr0) # Text Reset
COLOR_RED=$(tput setaf 1) # Red
BOLD=$(tput bold) # Bold


if ! [ -x "$(command -v steam)" ]; then
  echo ">> ${BOLD}${COLOR_RED}Error:${RESET} ${BOLD}Steam${RESET} is not installed." >&2
  exit 1
fi

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
