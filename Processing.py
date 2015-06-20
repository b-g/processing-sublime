import sublime, sublime_plugin, sys, functools, os, re, string

# NOTE: Change this next line to match the correct library path for your system.
DEFAULT_PROCESSING_LIBRARY_PATH = "/Applications/Processing.app/Contents/Java/core/library"
PROJECT_TEMPLATE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/Commands/templates/new_java_ant_project"
SOURCE_DIRECTORY_NAME = "src"
BUILDFILE_TEMPLATE_NAME = "build.xml.template"
GENERATED_BUILDFILE_NAME = "build.xml"
JAVA_TEMPLATE_FILENAMES = ["Main.java.template", "Sketch.java.template"]
SKETCH_FILE_NAME = "Sketch.java"
STATUS_MESSAGE = "New Java Ant Processing project created. Be sure to use the Ant build system, not JavaC."

class NewJavaAntProjectCommand(sublime_plugin.WindowCommand):

    def run(self):
        # TODO: app command w/o window: create window, self.window.run_command("prompt_add_folder")
        self.window.show_input_panel("Package Name:",
                                     "com.foo.appname or simplepackagename",
                                     functools.partial(self.generate_project),
                                     None, None)
  
    def generate_project(self, package_name):
        generated_source_path = os.path.join(self.window.folders()[0],
                                             SOURCE_DIRECTORY_NAME,
                                             re.sub('\.', '/', package_name.lower()))
        self.create_project_directories(generated_source_path)
        self.generate_files_from_template(PROJECT_TEMPLATE_PATH,
                                          generated_source_path,
                                          package_name)
        self.window.open_file(os.path.join(generated_source_path, SKETCH_FILE_NAME))
        sublime.status_message(STATUS_MESSAGE)
    
    def create_project_directories(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
  
    def generate_files_from_template(self, template_path, generated_source_path, package_name):
        self.generate_buildfile(template_path, package_name)
        self.generate_java_boilerplate(template_path, generated_source_path, package_name)
    
    def generate_buildfile(self, template_path, package_name):
        with open(os.path.join(template_path, BUILDFILE_TEMPLATE_NAME), 'r') as build_template:
            template = string.Template(build_template.read())
        with open(os.path.join(self.window.folders()[0], GENERATED_BUILDFILE_NAME), 'w') as buildfile:
            buildfile.write(template.substitute(ant_project_name = package_name.split('.')[-1],
                                                processing_library_path = self.determine_processing_library_path(),
                                                package_name = package_name))

    def generate_java_boilerplate(self, template_path, generated_source_path, package_name):
        for template_name in JAVA_TEMPLATE_FILENAMES:
            with open(os.path.join(template_path, template_name), 'r') as java_template:
                template = string.Template(java_template.read())
            with open(os.path.join(generated_source_path, template_name.rsplit('.', 1)[0]), 'w') as source_file:
                source_file.write(template.substitute(package_name = package_name))

    def determine_processing_library_path(self):
        # TODO: determine path from OS? Or use explicit settings.
        return DEFAULT_PROCESSING_LIBRARY_PATH

#open_file(file, contents)

# class NewFolderCommand(sublime_plugin.WindowCommand):
#     def run(self, dirs):
#         self.window.show_input_panel("Folder Name:", "", functools.partial(self.on_done, dirs[0]), None, None)

#     def on_done(self, dir, name):
#         os.makedirs(os.path.join(dir, name))

#     def is_visible(self, dirs):
#         return len(dirs) == 1
