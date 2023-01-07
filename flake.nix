{
  description = "Counter application";

  outputs = { self, nixpkgs }: {

    packages.x86_64-linux.default = import ./build.nix { pkgs = nixpkgs.legacyPackages.x86_64-linux; };
    packages.x86_64-linux.buildDocker = import ./buildDocker.nix { pkgs = nixpkgs.legacyPackages.x86_64-linux; main = self.packages.x86_64-linux.default; };
  };
}
