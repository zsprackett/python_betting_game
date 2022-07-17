{ pkgs }: {
  deps = [
    pkgs.python39Full
    pkgs.python39Packages.poetry
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      # Needed for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
      # Needed for matplotlib
      pkgs.xorg.libX11
    ];
    PYTHONBIN = "${pkgs.python39Full}/bin/python3.9";
    LANG = "en_US.UTF-8";
  };
}
