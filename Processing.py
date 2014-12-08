import sublime, sublime_plugin, sys, functools, os, re, string

#from plugins.new_java_project import *

PROJECT_TEMPLATE_PATH = os.path.abspath("Commands/templates/new_java_ant_project")
SOURCE_DIRECTORY_NAME = "src"
BUILDFILE_TEMPLATE_NAME = "build.xml.template"
GENERATED_BUILDFILE_NAME = "build.xml"

class NewJavaAntProjectCommand(sublime_plugin.WindowCommand):

    def run(self):
        # TODO: app command w/o window: create window, self.window.run_command("prompt_add_folder")
        self.window.show_input_panel("Package Name:",
                                     "com.foo.appname or simplepackagename",
                                     functools.partial(self.generate_project),
                                     None, None)
  
    def generate_project(self, package_name):
        project_path = os.path.join(self.window.folders()[0],
                                    SOURCE_DIRECTORY_NAME,
                                    re.sub('\.', '/', package_name.lower()))
        self.create_project_directories(project_path)
        self.generate_files_from_template(PROJECT_TEMPLATE_PATH,
                                          project_path,
                                          package_name)
    
    def create_project_directories(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
  
    def generate_files_from_template(self, template_path, project_path, package_name):
        processing_library_path = self.determine_processing_library_path()
        with open(os.path.join(template_path, BUILDFILE_TEMPLATE_NAME), 'r') as build_template:
            template_contents = build_template.read()
        template = string.Template(template_contents)
        build_file_contents = template.substitute(processing_library_path = processing_library_path,
                                                  ant_project_name = package_name.split('.')[-1],
                                                  package_name = package_name)
        with open(os.path.join(self.window.folders()[0], GENERATED_BUILDFILE_NAME), 'w') as buildfile:
            buildfile.write(build_file_contents)
  
    def determine_processing_library_path(self):
        return "TODO"

#open_file(file, contents)


# class NewFolderCommand(sublime_plugin.WindowCommand):
#     def run(self, dirs):
#         self.window.show_input_panel("Folder Name:", "", functools.partial(self.on_done, dirs[0]), None, None)

#     def on_done(self, dir, name):
#         os.makedirs(os.path.join(dir, name))

#     def is_visible(self, dirs):
#         return len(dirs) == 1