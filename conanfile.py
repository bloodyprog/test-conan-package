import os
from conans import ConanFile

channel = os.getenv("CONAN_CHANNEL", "channel")
username = os.getenv("CONAN_USERNAME", "username")

class TestPackage(ConanFile):
    settings = "os"

    def build(self):
        self.output.warn("BUILD...")

    def package(self):
        self.output.warn("PACKAGE...")
