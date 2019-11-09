import sublime, sublime_plugin, os
# super+shift+8

class CreateActionViewCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    region          = self.view.sel()[0]
    source          = self.view.file_name()
    source_path     = os.path.dirname(source)
    rails_view_path = os.path.dirname(source_path)
    views_path      = source.replace('controllers', 'views').split('_controller.rb')[0]
    actions         = []
    all_defs        = self.view.find_all(' def ')

    for d in all_defs:
      if d < region:
        line        = self.view.line(d)
        line_text   = self.view.substr(line)
        action_name = line_text.split('def ')[1].strip()
        actions.append(action_name)

    layouts_folder = rails_view_path + '/views/layouts/'
    for file in os.listdir(layouts_folder):
        if 'application' in file:
            extension = file.split('.')[1]

    views_path_with_file_name = views_path + '/' + action_name + '.' + extension

    if not os.path.exists(views_path_with_file_name):
      open(views_path_with_file_name, 'w')
      self.view.window().open_file(views_path_with_file_name)