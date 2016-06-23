import os
from conans import ConanFile
from conans.tools import download, unzip

channel = os.getenv("CONAN_CHANNEL", "channel")
username = os.getenv("CONAN_USERNAME", "username")

class TestPackage(ConanFile):
    name = "test-package"
    version = "0.1"
    settings = "os"

    def build(self):
        archive = "premake.zip"
        download("https://github.com/premake/premake-core/releases/download/v5.0.0-alpha9/premake-5.0.0-alpha9-src.zip", archive)
        unzip(archive)
        os.unlink(archive)

        if self.settings.os == "Windows":
            os.chdir("premake-5.0.0-alpha9/build/gmake.windows")
            self.run("nmake")
            os.chdir("../..")

        elif self.settings.os == "Macos":
            os.chdir("premake-5.0.0-alpha9/build/gmake.macosx")
            self.run("make")

        elif self.settings.os == "Linux":
            os.chdir("premake-5.0.0-alpha9/build/gmake.unix")
            self.run("make")

    def package(self):
        self.copy("*", dst="bin", src="premake-5.0.0-alpha9/bin/release")
