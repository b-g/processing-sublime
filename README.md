# Processing Package for Sublime Text

A [Processing](http://processing.org/) package for [Sublime Text 2 and 3](http://www.sublimetext.com/). Check the [demo video](https://vimeo.com/45573600) on vimeo!
Please note: you must have at least (>=Processing 2.0b6), otherwise the build system of the this package won't work. The video is a bit outdated, you don't have to run any longer the Processing.app in parallel to run sketches. If you have to use an old Processing version (e.g. 1.5.1), you can use [version 1.0 of this package](https://github.com/b-g/processing-sublime/releases/tag/v1.0_Processing_1.5.1).

[<img src="https://github.com/b-g/processing-sublime/raw/master/Images/overview.png">](https://vimeo.com/45573600)


## Preparations
### OSX
Use Processing's _Tools > Install "processing-java"_ menu item after you have installed Processing.

![Use external editor preference](https://github.com/b-g/processing-sublime/raw/master/Images/processing_preferences.gif "Use external editor preference")

This package assumes that you chose to install `processing-java` for all users (recommended). If you choose to install `processing-java` only in your home directory, then you have to slightly change the build script, see the comment in the file [Processing.sublime-build](https://github.com/b-g/processing-sublime/blob/master/Build%20Systems/Processing.sublime-build).

### Linux
You will need to set your `PATH` to where your processing application is located, e.g.:
`export PATH=$PATH:/opt/processing/processing-2.0b4`

You also need to create an alias for `processing-java` in `/bin/` instead of `/usr/bin/`, e.g.:
`sudo ln -s /opt/processing/processing-java /bin/processing-java`

### Windows
You will need to set your `PATH` environment variable to where your processing application is located:

- Open the "Advanced System Settings" by running `sysdm.cpl`
- In the "System Properties" window, click on the _Advanced_ tab.
- In the "Advanced" section, click the _Environment Variables_ button.
- Edit the "Path" variable. Append the processing path (e.g. `;C:\Program Files\Processing-2.0b6\`) to the variable value. Each entry is separated with a semicolon.

Or, write a separate build system as documented in this [comment](https://github.com/b-g/processing-sublime/issues/17#issuecomment-15585500).

![Advanced System Settings > Environment Variables](https://github.com/b-g/processing-sublime/raw/master/Images/processing_path_windows.gif "Windows Environment Variables")


## Installation
There are three easy ways to install the Processing package:

### Using Sublime Package Control
If you are using [Sublime Package Control](https://packagecontrol.io/), you can easily install the [Processing Package](https://packagecontrol.io/packages/Processing) via the _Sublime Text > Preferences > Package Control: Install Package_ menu item.

### Using Git
Alternatively you can install the package and keep up to date by cloning the repo directly into your Sublime Text `Packages` directory.

Go to your Sublime Text `Packages` directory and clone this repository:
`git clone https://github.com/b-g/processing-sublime/ Processing`

### Download Manually
- Download the files using the GitHub [.zip download option](https://github.com/b-g/processing-sublime/archive/master.zip).
- Unzip the file and rename the directory to `Processing`.
- Copy the directory to your Sublime Text `Packages` directory e.g. OS X: `~/Library/Application Support/Sublime Text 2/Packages/Processing`.


## Usage
- Open the directory containing a Processing sketch in Sublime Text. (e.g. Drag the folder to Sublime Text.)
- In Sublime Text, select the _Tools > Build System > Processing_ menu item.
- In Sublime Text, select your main `.pde` file and use **⌘B** to run the sketch. The build system expects that your sketch follows the normal directory structure and naming conventions of a Processing sketch (e.g. `mysketch/mysketch.pde`).
- With **⇧⌘B** and typing `build`, you can select alternative build systems, such as _Run sketch fullscreen_ and various _Export sketch_ options.

### Custom shortcuts
To get `.pde` files to run with **⌘R** and **⇧⌘R** (like Processing) instead of **⌘B** and **⇧⌘B**, add the following code to the User Key Bindings file via the _Preferences > Key Bindings - User_ menu item in Sublime Text.

```
{
  "keys": ["super+r"], "command": "build",
  "context": [{ "key": "selector", "operator": "equal", "operand": "source.pde" }]
},
{
  "keys": ["super+shift+r"], "command": "build",
    "args": {"variant": "Run sketch fullscreen"},
    "context": [{ "key": "selector", "operator": "equal", "operand": "source.pde" }]
}
```

### Console errors
Console error messages are clickable: e.g. double click `test.pde:10:0:10:0: The function rEEct(int, int, int, int) does not exist` to jump to the related line and file.


## Want a "Pure Java" Project without Eclipse?

Complex projects often lead people into using Processing with [Eclipse](http://eclipse.org). If you want to stick with Sublime Text, but want a "pure Java" Processing project _and_ the convenience of a fast "build and run" workflow, try creating a project with the _New Java Ant Project_ command (see [issue 61](https://github.com/b-g/processing-sublime/issues/61)) and run your sketch with the _Ant_ build system.

### Prerequisites
Be sure that [ant](http://ant.apache.org/) is installed and on your environment's `PATH`. You know this is right when you can open a terminal, run `ant`, and see a `Build failed` message. This means that [ant](http://ant.apache.org/) is runnable, and failing is ok because there is no "Buildfile."

Make sure that the variable `DEFAULT_PROCESSING_LIBRARY_PATH` within the file `Processing.py` inside this package matches your installation of Processing. If you are on OS X and `Processing.app` is in the `Applications` directory, then you do not need to edit this. Despite this, OS X users may need to install the [Fix Mac Path](https://packagecontrol.io/packages/Fix%20Mac%20Path) package, due to the way Sublime manages environment variables such as `PATH`.

### Using the Command

1. Create an empty directory (folder) for your new project, and open that empty directory in Sublime.
2. Use either the menu item _Tools > Processing > New Java Ant Project_ or select the _Processing: New Java Ant Project_ command from the command pallete (**⇧⌘P**).
3. Specify a Java package name for your source code (e.g. `com.myorg.myapp`).
4. Use the _Tools > Build System > Ant_ menu item to ensure that _Ant_ is the active build system.
5. Use **⌘B** to build and run your sketch. Out of the box, you should see a full screen app that displays the default 200x200px gray sketch, which is the Processing default.

You can now implement `setup` and `draw`, add additional classes to your sketch, and run it with **⌘B**. Just be sure that _Ant_ is the active build system.


## Getting Started with Sublime Text
If you are new to Sublime I recommend the [Perfect Workflow in Sublime Text](http://code.tutsplus.com/courses/perfect-workflow-in-sublime-text-2) tutorial. If you are short of time, then make sure to at least watch [Multiple Cursors and Incremental Search](http://code.tutsplus.com/courses/perfect-workflow-in-sublime-text-2/lessons/multiple-cursors-and-incremental-search) (~6min), highly recommended!


## Acknowledgements
- Original [Processing TextMate Bundle](http://www.onebitwonder.com/projects/processing/): [Leon Hong](http://www.onebitwonder.com/)
- Textmate to Sublime snippet conversion: [textmate-to-sublime-converter](https://github.com/srbs/textmate-to-sublime-converter)
- Maintainer: [Benedikt Groß](http://benedikt-gross.de/log/)
- Syntax highlighting tweaking: [Mark Brand](https://github.com/ignism)
- Linux build script and testing: [Julien Deswaef](http://xuv.be/)
- Windows build script and documention: [Ralf Baecker](http://github.com/rlfbckr)
- Error console capturer: [Greger Stolt Nilsen](http://gregerstoltnilsen.net/)
- Syntax definition, snippet cleansing, Processing reference vs. sublime [diff tool](https://github.com/ybakos/processing-sublime-util), and _New Java Ant Project_ command: [Yong Joseph Bakos](http://yongbakos.com)
- How to set custom shortcuts: [Raphaël de Courville](https://github.com/SableRaf)
- Rebuild of the processing syntax highlighter: [Kyle Fleming](https://github.com/kylefleming)

See the [contributing guide](https://github.com/b-g/processing-sublime/blob/master/CONTRIBUTING.md) to learn about how to contribute to this project.

