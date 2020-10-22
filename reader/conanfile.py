from conans import ConanFile
import os

EXE_NAME = 'calc_obb_from_txt'

class HelloPythonConan(ConanFile):
    name = "reader"
    version = "0.1"
    exports = '*'
    build_policy = "missing"
    requires = "obb/0.1@ar/stable"

    def build(self):
        self.run('pyinstaller --onefile ' + EXE_NAME + '.py')

    def package(self):
        self.copy('*.py')
        self.copy(EXE_NAME, src='dist', dst='bin')

    def package_info(self):
        self.env_info.PYTHONPATH.append(self.package_folder)
        self.env_info.PATH.append(os.path.join(self.package_folder, 'bin'))
