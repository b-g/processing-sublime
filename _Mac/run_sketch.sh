
if [ -n "$1" ]
	then
		BN=$(basename "$1")
		IS_OPEN=$(osascript ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Processing/_Mac/isProcessingOpen.scpt)

		if test $IS_OPEN -gt 0
			then
				echo "### Run Processing Sketch: $BN.pde "
				open -a Processing "$1/$BN.pde"
				osascript ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Processing/_Mac/runOpenSketch.scpt
				exit 0
			else
				echo "### ERRROR: Ups ... Processing is not open :("
				echo "Please make sure Processing.app is open and 'Use external editor' in Processing preferences in checked."
				exit 1
		fi

	else
		echo "### ERRROR: No open file ... No Processing file to run :("
		echo "Please open a file in a tab in Sublime"
		exit 1
fi