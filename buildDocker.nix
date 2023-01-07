{ pkgs, main }:

pkgs.dockerTools.buildImage {
  name = "counter";
  copyToRoot = pkgs.buildEnv {
    name = "image-root";
    paths = [ main ];
    pathsToLink = ["/bin"];
  };
  config = {
    Cmd = ["/bin/main"];
  };
}
