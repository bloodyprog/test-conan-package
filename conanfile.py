import os
from conans import ConanFile

channel = os.getenv("CONAN_CHANNEL", "channel")
username = os.getenv("CONAN_USERNAME", "username")

class TestPremake(ConanFile):
    settings = "os"
    requires = "test-package/0.1@%s/%s" % (username, channel)

    def imports(self):
        self.output.warn("IMPORTS...")

    def build(self):
        self.output.warn("BUILD...")

    def package(self):
        self.output.warn("PACKAGE...")
