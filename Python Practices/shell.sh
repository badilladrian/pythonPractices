#!/bin/bash
rm -f _txt_ _tt _tempo_ lista lista2 *.raw* clockinout.xls  2>/dev/null
clear
printf "\nInterviewer Clock IN-OUT Utility\n================================\n\n"
while true
do
	printf "\nPlease enter START date YYYYMMDD: "	
	read sdate	
	printf "\nPlease enter END date YYYYMMDD: "	
	read edate	
	printf "\n\nIs date range $sdate - $edate correct (y/n)? "	
	read yn	
	if [ $yn == "y" ] ; then	
		break	
	fi	
done

clear
printf "\nEmployee Selection\n\n1. ALL Employees\n2. Select specific Employees\n\nChoose an option: "
read choice

if [ $choice == "2" ] ; then

	while true
	do
		clear
		printf "\nDATE RANGE: $sdate - $edate\n\n---------------------------------------------------------------------\n\nPlease enter Interviewer IDs. (Press <ENTER> then CTRL+D when done)\nUse <ENTER> for several IDs. Example:\n(1 interviewer)\n3022\n\n(4 interviewers)\n3035\n3038\n3044\n3055\n\n---------------------------------------------------------------------\nEnter IDs: \n"
		pte.pl
		clear
		printf "Entered IDS:\n\n"
		cat _txt_
		printf "\nAre the above interviewers correct (y/n)? "
		read yn
		if [ $yn == "y" ] ; then
			cat _txt_ | awk '{ if ($0 !~ /^$/) { print $0;} }' > _tt
			mv _tt _txt_
			break
		fi
	done

else
	cat /cfmc/control/employee.xxx | awk '{ print $1}' | sort -n > _txt_	
	cat _txt_ | awk '{ if ($0 !~ /^$/) { print $0;} }' > _tt
	mv _tt _txt_
fi

printf "\n\nProcessing Report... Please wait...\n\n"

ls intvrlog.* > lista
file="lista"
exec 3<$file
while read -u3 line
do
	fecha=`echo $line | awk '{t=split($0,a,"."); gsub(/_/,"",a[t]); print a[t];}'`
	
	if [ $fecha -ge $sdate ] && [ $fecha -le $edate ] ; then
		echo $line >> lista2 
	fi
done
exec 3<&-

printf "INTERVIEWER ID\tINTERVIEWER NAME\tDATE\tSTART TIME\tEND TIME\tHOURS (including ALL breaks)\tDIALED PROJECTS\tEXTENSIONS\tBREAK TIME HOURS\tLUNCH TIME HOURS\tMEETING TIME HOURS\tBREAK TIME DISCOUNT HOURS (if applicable)\tLUNCH TIME PAID HOURS\tPAID HOURS\n" > clockinout.xls

inters=`cat _txt_`

file="lista2"
exec 3<$file
while read -u3 line
do
	fecha=`echo $line | awk '{t=split($0,a,"."); gsub(/_/,"",a[t]); print a[t];}'`
	file2="_txt_"
	exec 4<$file2
	while read -u4 line2
	do
		grep "^${line2}" $line > ${line2}.raw1
		if [ -s ${line2}.raw1 ] ; then
			gawk -f clockio.awk ${line2}.raw1 | sort -n > ${line2}.raw2	
			gawk -f getinfo.awk ${line2}.raw2 > _tempo_
			
			studies=`head -1 _tempo_`
			exts=`tail -1 _tempo_`

			stime=`head -1 ${line2}.raw2 | awk '{ print substr($1,9,2)":"substr($1,11,2); }'`
			etime=`tail -1 ${line2}.raw2 | awk '{ print substr($2,9,2)":"substr($2,11,2); }'`

			stimef=`head -1 ${line2}.raw2 | awk '{ print $1; }'`
			etimef=`tail -1 ${line2}.raw2 | awk '{ print $2; }'`

			diff=`perl time.pl $stimef $etimef`

			hours=`echo $diff | awk '{ min=$0/60; hr=min/60; hrs=sprintf("%.2f",hr); print hrs;}'`

			name=`head -1  ${line2}.raw2 | awk '{ split($0,a,"|"); print a[2];}'`	

			str=`cat ${line2}.raw2 | awk ' BEGIN{} {split($0,a,"|"); tbreak=tbreak+a[7]; tlunch=tlunch+a[8]; tmeety=tmeety+a[9];} END{print tbreak/60/60"\t"tlunch/60/60"\t"tmeety/60/60;} '`


			tlunch=`cat ${line2}.raw2 | awk ' BEGIN{} { split($0,a,"|"); tbreak=tbreak+a[7]+0; tlunch=tlunch+a[8]; } END{ print tlunch/60/60; } '`
			tbreak=`cat ${line2}.raw2 | awk ' BEGIN{} { split($0,a,"|"); tbreak=tbreak+a[7]+0; tlunch=tlunch+a[8]; ; } END{ print tbreak/60/60; } '`

			#if echo ${hours} | awk '{exit !( $1 >= 3 && $1 < 6)}'; then tpaid=0.25; fi
			#if echo ${hours} | awk '{exit !( $1 >= 6 && $1 < 8)}'; then tpaid=0.33333; fi
			#if echo ${hours} | awk '{exit !( $1 >= 8 && $1 < 10)}'; then tpaid=0.416667; fi
			#if echo ${hours} | awk '{exit !( $1 >= 10)}'; then tpaid=0.5; fi

#            if echo ${hours} | awk '{exit !( $1 >= 4 && $1 < 5)}'; then tpaid=0.25; fi
#            if echo ${hours} | awk '{exit !( $1 >= 5 && $1 < 6)}'; then 
#            if echo ${hours} | awk '{exit !( $1 >= 7 && $1 < 8)}'; then tpaid=0.4333; fi
#            if echo ${hours} | awk '{exit !( $1 >= 8 && $1 < 9)}'; then tpaid=0.5; fi
#            if echo ${hours} | awk '{exit !( $1 >= 9 && $1 < 10)}'; then tpaid=0.5666; fi
#            if echo ${hours} | awk '{exit !( $1 >= 10 && $1 < 12)}'; then tpaid=0.6166; fi
#            if echo ${hours} | awk '{exit !( $1 >= 12)}'; then tpaid=0.75; fi



#New Break Scheme 2019-09-05
#            if echo ${hours} | awk '{exit !( $1 >= 7 && $1 <= 8)}'; then tpaid=0.30; fi
#            if echo ${hours} | awk '{exit !( $1 >= 8.15 && $1 <= 9)}'; then tpaid=0.34; fi
#            if echo ${hours} | awk '{exit !( $1 >= 9.15 && $1 <= 10)}'; then tpaid=0.38; fi
#            if echo ${hours} | awk '{exit !( $1 > 10 )}'; then tpaid=0.38; fi




#New Break/Lunch Scheme 2019-11-04


			tlunchpaid=0
            if echo ${hours} | awk '{exit !( $1 >= 3 && $1 < 4)}'; then tlunchpaid=0.25; fi
            if echo ${hours} | awk '{exit !( $1 >= 4 && $1 < 5)}'; then tlunchpaid=0.316; fi
            if echo ${hours} | awk '{exit !( $1 >= 5 && $1 < 6)}'; then tlunchpaid=0.383; fi
            if echo ${hours} | awk '{exit !( $1 >= 6 && $1 < 8)}'; then tlunchpaid=0.5; fi
            if echo ${hours} | awk '{exit !( $1 >= 8 && $1 < 9)}'; then tlunchpaid=0.56; fi
            if echo ${hours} | awk '{exit !( $1 >= 9 && $1 < 10)}'; then tlunchpaid=0; fi
            if echo ${hours} | awk '{exit !( $1 >= 10)}'; then tlunchpaid=0; fi

		
			tbrkpaid=0
            if echo ${hours} | awk '{exit !( $1 < 4)}'; then tbrkpaid=0; fi
            if echo ${hours} | awk '{exit !( $1 >= 4 && $1 < 6)}'; then tbrkpaid=0.166; fi
            if echo ${hours} | awk '{exit !( $1 >= 6 && $1 < 8)}'; then tbrkpaid=0.25; fi
            if echo ${hours} | awk '{exit !( $1 >= 8 && $1 < 10)}'; then tbrkpaid=0.3; fi
            if echo ${hours} | awk '{exit !( $1 >= 10)}'; then tbrkpaid=0.3; fi





			ttbreak=`echo ${str} | awk '{split($0,a,"\t"); print $1;}'`
			ttlunch=`echo ${str} | awk '{split($0,a,"\t"); print $2;}'`

			ttpaid=0

			ttpaid=`paidhours.py ${hours} ${tlunchpaid} ${tbrkpaid} ${tlunch} ${tbreak}`



			printf "${line2}\t${name}\t${fecha}\t${stime}\t${etime}\t${hours}\t${studies}\t${exts}\t${str}\t${tbrkpaid}\t${tlunchpaid}\t${ttpaid}\n" >> clockinout.xls	
		fi
	done
	exec 4<&-
done
exec 3<&-

if [ -s clockinout.xls ] ; then

while true
do
        clear
        printf "\n\nPlease type email address where you want to send the report to?\n"
        read email
        printf "\nIs $email correct (y/n)?"
        read ok
        if [ $ok == "y" ] ; then

/usr/local/bin/email -c email.conf -s "Clock IN-OUT Report $sdate - $edate" -b $email -a clockinout.xls <<txt

Attached you will find the clock IN-OUT report from $sdate to $edate , for the following interviewers:
${inters}
txt
		printf "\n\nEmail sent!!!\n\n"
                break
        fi
done
fi
