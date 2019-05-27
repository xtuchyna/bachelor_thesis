#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
	fedpkg clone --anonymous $line && cd $line
	fedpkg srpm
	rpm -qp --requires ${line}*.src.rpm > $line
	mv $line ../dependencies/${line}.txt
	cd ..
	rm -rf $line
done < "$1"
