# This script configures all the required variables and files
# required for the deployment of student Jupyter notebooks
# in Fred Passeron LR4 
#
# NOTE: it modifies the InfraConfig.yml which sets Ansible variables.
#
# It is called by the TotalReset.sh script
#
# Version 0.5

# Configure the remote location
#Location="FdzETC" 
#Location="PfLR5" 
Location="FpLR4" 

# Workshop Range in Mougins (notebooks): 51-100
# Challenge Range in Gre (notebooks2): 61-99
capacity="62"
myrange="61-{{capacity}}"
workshop="WKSHP-RedfishOverview"



############################ Don't modify below ###################
JupyterLocation="JupyterIn${Location}"
BastionLocation="BastionIn${Location}"

Resp=""
read -p "Ok to deploy Workshop/Challenge $workshop on $Location ? " Resp
while true ; do
	case $Resp in
		[Yy]* )
			echo "Progressing..."
			break;;
		[Nn]* )
			echo "So, just modify InfraConfig.sh to change the Target"
			exit;;
		* )
			echo "Answer should be Y,y,N or n"
			exit;;
	esac
done

Resp=""
read -p "Ok to deploy with capacity=${capacity} and myrange=${myrange} ? " Resp
while true ; do
	case $Resp in
		[Yy]* )
			echo "Super! Let's go..."
			break;;
		[Nn]* )
			echo "So, just modify Infraconfig.sh to change the capacity and myrange"
			exit;;
		* )
			echo "Answer should be Y,y,N or n"
			exit;;
	esac
done


# Set bastion IP and ssh port according to the Jupyter location
case $Location in
	FdzETC ) 
		BastionIP=fdz580g8
		BastionSshPort=22
		ObmcHostGroup="OpenbmcsInFdzETC"
		;;
	PfLR5 )
		BastionIP=pfisaserver
		BastionSshPort=921
		ObmcHostGroup="OpenbmcsInPfLR5"
		;;
	FpLR4 )
		BastionIP=localhost
		BastionSshPort=1188
		ObmcHostGroup="OpenbmcsInFpLR4"
		CreateSshTunnel=1
		;;
	* )
		echo "Problem with Bastion IP and Port. Exiting..."
		exit;;
esac

SED="`which sed` -i "
SSH="`which ssh` -p $BastionSshPort "
Username="francois"
#ObmcsUsername="root"
APB="`which ansible-playbook` -i hosts "

# Prepare yml files with correct Jupyter and Obmc host locations
$SED 's/\(^capacity: \).*$/\1'${capacity}'/; s/\(^myrange: \).*$/\1'${myrange}'/' \
	InfraConfig.yml
$SED 's/\(^workshop: \).*$/\1"'${workshop}'"/' \
	InfraConfig.yml

$SED 's/\(^- hosts:\).*$/\1 '${ObmcHostGroup}'/' \
	ConfigureStudentObmcs.yml \
	StartStudentObmcs.yml

#$SED 's/\(^- hosts:\).*$/\1 '${JupyterLocation}'/' \
        #CopyStudentFolder.yml \
        #CopyDevFolder.yml     \
	#KillSomeStudentServers.yml \
	#KillAllUserServers.yml

echo


