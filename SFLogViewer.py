#Generally using the code of scrub log from MavensMate

import sublime
import sublime_plugin
import os

class ScrubLogCommand(sublime_plugin.WindowCommand):
    def run(self):
        active_view = self.window.active_view()
        fileName, ext = os.path.splitext(active_view.file_name())

        lines = []
        new_lines = []

        with open(active_view.file_name()) as f:
            lines = f.readlines()

        for file_line in lines:
            if '|USER_DEBUG|' in file_line and '|DEBUG|' in file_line:
                new_lines.append(file_line)
            elif '|EXCEPTION_THROWN|' in file_line or '|FATAL_ERROR|' in file_line:
                new_lines.append(file_line)

        string = "\n".join(new_lines)
        new_view = self.window.new_file()
        if "linux" in sys.platform or "darwin" in sys.platform:
            new_view.set_syntax_file(os.path.join("Packages","MavensMate","sublime","lang","MMLog.tmLanguage"))
        else:
            new_view.set_syntax_file(os.path.join("Packages/MavensMate/sublime/lang/MMLog.tmLanguage"))
        new_view.set_scratch(True)
        new_view.set_name("Scrubbed Log")

        size = new_view.size()
        new_view.set_read_only(False)

        new_view.run_command('append', { 'characters': string, 'force': True, 'scroll_to_end': False })
        #new_view.insert(edit, size, string)
        new_view.show(size)
