{ pkgs, main }:

pkgs.dockerTools.buildImage {
  name = "counter";
  tag = "latest";

  copyToRoot = pkgs.buildEnv {
    name = "image-root";
    paths = [ main ];
    pathsToLink = ["/bin"];
  };
  config = {
    Cmd = ["/bin/main"];
  };
}
