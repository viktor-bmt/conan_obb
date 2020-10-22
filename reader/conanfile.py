from conans import ConanFile

class HelloPythonConan(ConanFile):
    name = "reader"
    version = "0.1"
    exports = '*'
    build_policy = "missing"
    requires = "obb/0.1@ar/testing"

    def package(self):
        self.copy('*.py')

    def package_info(self):
        self.env_info.PYTHONPATH.append(self.package_folder)