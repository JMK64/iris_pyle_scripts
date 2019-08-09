#! /usr/bin/env bash
# declare -a zzStashArr=("50156" "50157" "34009" "50158" "34010" "50159" "34011" "50160" "34014" "50161" "34018" "50162" "34022" "50163" "34016" "50164" "34027" "50172")
declare -a zzStashArr=( "30451")
declare -a zzJobID=u-ba471
declare -a zzTempDir=/group_workspaces/jasmin4/htap2/ptg21/${zzJobID}/pp_files_oh/
mkdir -p ${zzTempDir}

cp call_template ${zzTempDir}/call_template

cd ${zzTempDir}

for zzStash in ${zzStashArr[@]};do
	mkdir -p ${zzStash}
	cd ${zzStash}
	echo ${zzStash} # check
	cp ../call_template call_edit.dat
	sed "s/PHSTASH/${zzStash}/g" call_edit.dat > call_active.dat
	/opt/moose/external-client-version-wrapper/bin/moo select ${zzTempDir}/${zzStash}/call_active.dat moose:crum/${zzJobID}/apm.pp ${zzTempDir}/${zzStash}
	#/opt/moose/external-client-version-wrapper/bin/moo select ${zzTempDir}/${zzStash}/call_active.dat moose:crum/${zzJobID}/apy.pp ${zzTempDir}/${zzStash}
	# mv *.pp ${zzOutputDir}/
	cd ../
done
