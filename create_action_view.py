import sublime, sublime_plugin, os
# super+shift+8

class CreateActionViewCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    region      = self.view.sel()[0]
    file_name   = self.view.file_name()
    views_path  = file_name.replace('controllers', 'views').split('_controller.rb')[0]
    extension   = self.detect_extensiton(file_name)
    action_name = self.detect_action_name(region)
    file_path   = views_path + '/' + action_name + '.' + extension

    self.create_view_folder(views_path)
    self.create_view_file(file_path)

  def detect_action_name(self, region):
    all_defs    = self.view.find_all(' def ')
    for d in all_defs:
      if d < region:
        line        = self.view.line(d)
        line_text   = self.view.substr(line)
        return line_text.split('def ')[1].strip()

  def detect_extensiton(self, file_name):
    file_path       = os.path.dirname(file_name)
    rails_view_path = os.path.dirname(file_path)
    layouts_folder = rails_view_path + '/views/layouts/'
    for file in os.listdir(layouts_folder):
      if 'application' in file:
        return file.split('.')[1]

  def create_view_folder(self, views_path):
    if not os.path.exists(views_path):
      os.mkdir(views_path)

  def create_view_file(self, file_path):
    if not os.path.exists(file_path):
      open(file_path, 'w')
      self.view.window().open_file(file_path)