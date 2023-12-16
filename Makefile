# example: make new_day DAY=_07
YEAR=2023

new_day:
	mkdir ${YEAR}/${DAY}
	cp ${YEAR}/adventofcode.py ${YEAR}/${DAY}
	touch ${YEAR}/${DAY}/test.txt
	touch ${YEAR}/${DAY}/input.txt