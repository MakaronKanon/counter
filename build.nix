{ pkgs ? import <nixpkgs> {}}:

pkgs.buildGoModule {
  name = "counter";
  vendorHash = null;
  src = ./.;
}
