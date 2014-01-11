# Processing Bundle for Sublime Text 2

A [Processing](http://processing.org/) bundle for [Sublime Text 2](http://www.sublimetext.com/2). Check the [demo video](https://vimeo.com/45573600) on vimeo!
Please note: you must have at least (>=Processing 2.0b6), otherwise the buildsystem of the this bundle won't work. The video is a bit outdated, you don't have to run any longer the Processing.app in parallel to run sketches. If you have to stick for some reason to an old Processing verion e.g. 1.5.1 you can use the [old version](https://github.com/b-g/processing-sublime/tags) of this bundle.

[<img src="https://github.com/b-g/processing-sublime/raw/master/Images/overview.png">](https://vimeo.com/45573600)

## Preparations
###OSX
Make sure to run `Tools -> Install "processing-java"` after you have installed the Processing.app.

![Use external editor preference](https://github.com/b-g/processing-sublime/raw/master/Images/processing_preferences.gif "Use external editor preference")

This bundle assumes that you chose to install processing-java for all users (recomended). If you choose/have to install processing-java only in your home directory, then you have to slightly change the build script, see comment in `Processing.sublime-build`.

###Linux
You will need to set your PATH to where your processing application is located, e.g.:
`export PATH=$PATH:/opt/processing/processing-2.0b4`

###Windows
You will need to set your PATH environment variable to where your processing application is located:
- Open the "Advanced System Settings". e.g. by running "sysdm.cpl"
- In the System Properties window, click on the Advanced tab.
- In the Advanced section, click the Environment Variables button.
- Edit the "Path" variable. Append the processing path (e.g.: `;C:\Program Files\Processing-2.0b6\`) to Variable value.
  Each entry is separated with a semicolon.

or write a seperate build system as documented in this [comment](https://github.com/b-g/processing-sublime/issues/17#issuecomment-15585500)

![Advanced System Settings -> Environment Variables](https://github.com/b-g/processing-sublime/raw/master/Images/processing_path_windows.gif)

## Installation
There are 3 easy ways to install the Processing Bundle:

### Using Sublime Package Control
If you are using [Sublime Package Control](http://wbond.net/sublime_packages/package_control), you can easily install the Processing Bundle via the `Sublime Text 2 -> Preferences -> Package Control: Install Package` menu item.

### Using Git
Alternatively you can install the theme and keep up to date by cloning the repo directly into your `Packages` directory in the Sublime Text 2 application settings area.

Go to your Sublime Text 2 `Packages` directory and clone the theme repository using the command below:
`git clone https://github.com/b-g/processing-sublime/ "Processing"`

### Download Manually
- Download the files using the GitHub .zip download option
- Unzip the files and rename the folder to `Processing`
- Copy the folder to your Sublime Text 2 `Packages` directory e.g. OS X: `~/Library/Application Support/Sublime Text 2/Packages/Processing`

## Usage
- Select in Sublime Text the Processing buildsystem: `Tools -> Build system -> Processing`
- Run the sketch: `cmd+b` (make sure that you have the normal sketch structure of a folder and a pde-file: mysketch/mysketch.pde)
- With `cmd+shift+b` and typing `build` you get alternative buildsystems: `Run sketch fullscreen` and various `Export sketch options`

## Hints
- Console error messages are clickable: e.g. double click `test.pde:10:0:10:0: The function reect(int, int, int, int) does not exist.` to jump to the related line and file.

## Getting Start With Sublime Text
If you are new to Sublime I recommend the excellent and free video tutorial by nettuts: [Perfect Workflow in Sublime Text](http://net.tutsplus.com/articles/news/perfect-workflow-in-sublime-text-free-course/). If you are short of time, then make sure to watch at least the lession [Multiple Cursors and Incremental Search]( https://tutsplus.com/lesson/multiple-cursors-and-incremental-search/) (~6min), highly recommended!

## Acknowledgements
- This bundle is very much based on [Processing TextMate Bundle by Leon Hong](http://www.onebitwonder.com/projects/processing/), thanks for all the good work!
- I used the [textmate-to-sublime-converter](https://github.com/srbs/textmate-to-sublime-converter) to convert the snippets from the original Processing TextMate Bundle to Sublime Text speak.
- Syntax highlighting tweaking [Mark Brand](https://github.com/ignism)
- Linux build script and testing [Julien Deswaef](http://xuv.be/)
- Windows build script and documention [Ralf Baecker](http://github.com/rlfbckr)
- Error console capturer [Greger Stolt Nilsen](http://gregerstoltnilsen.net/)
- Master of the syntax definition. Whitespace and indentation cleanup. Processing reference vs. sublime [diff tool](https://github.com/ybakos/processing-sublime-util). [Yong Joseph Bakos](http://yongbakos.com/).
