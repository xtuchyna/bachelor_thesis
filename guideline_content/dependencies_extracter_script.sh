for packageName in `dnf repoquery --disablerepo=\* --enablerepo=fedora-source --qf '%{NAME}'`; do
	echo -n processing ${packageName}
	dnf repoquery --disablerepo=\* --enablerepo=fedora-source --requires $packageName > ./dependencies_extracted_from_specs/${packageName}.txt
done
