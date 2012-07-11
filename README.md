# Processing Bundle for Sublime Text 2
A [Processing](http://processing.org/) bundle for [Sublime Text 2](http://www.sublimetext.com/2).

[Check the demo video on vimeo!](https://vimeo.com/45573600)

###Mac OSX
![Overview](https://github.com/b-g/processing-sublime/raw/master/_Mac/overview.png "Overview")
Fully supported: snippets + buildsystem.

###Linux & Windows
Only partly supported: snippets, but no buildsystem.



## Installation
There are 3 easy ways to install the Processing Bundle:

### Using Sublime Package Control
Coming, currently pending ...
<!---
If you are using [Sublime Package Control](http://wbond.net/sublime_packages/package_control), you can easily install the Processing Bundle via the `Sublime Text 2 -> Preferences -> Package Control: Install Package` menu item.
-->

### Using Git
Alternatively you can install the theme and keep up to date by cloning the repo directly into your `Packages` directory in the Sublime Text 2 application settings area.

Go to your Sublime Text 2 `Packages` directory and clone the theme repository using the command below:
`git clone https://github.com/b-g/processing-sublime/ "Processing"

### Download Manually
- Download the files using the GitHub .zip download option
- Unzip the files and rename the folder to `Processing`
- Copy the folder to your Sublime Text 2 `Packages` directory e.g. OS X: `~/Library/Application Support/Sublime Text 2/Packages/Processing`



## Usage
- The Processing.app has to be open and 'Use external editor' in Processing preferences has to be checked.
![Use external editor preference](https://github.com/b-g/processing-sublime/raw/master/_Mac/processing_preferences.gif "Use external editor preference")

- Select in Sublime Text the Processing buildsystem: `Tools -> Build system -> Processing`

- Run the sketch: `cmd+b`


## Acknowledgements
- This bundle is very much based on [Processing TextMate Bundle by Leon Hong](http://www.onebitwonder.com/projects/processing/), thanks for all the good work!
- I used the [textmate-to-sublime-converter](https://github.com/srbs/textmate-to-sublime-converter) to convert the snippets from the original Processing TextMate Bundle to Sublime Text speak.
- My contribution is only the buildsystem and that finally someone did it :)