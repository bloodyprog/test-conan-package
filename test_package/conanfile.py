import os
from conans import ConanFile

channel = os.getenv("CONAN_CHANNEL", "channel")
username = os.getenv("CONAN_USERNAME", "username")

class TestTestPackage(ConanFile):
    settings = "os"
    requires = "test-package/0.1@%s/%s" % (username, channel)

    def imports(self):
        self.output.warn("IMPORTS...")
        self.copy("*", dst="bin", src="bin")

    def build(self):
        self.output.warn("BUILD...")

    def test(self):
        self.output.warn("TEST...")
        self.run("ls")
