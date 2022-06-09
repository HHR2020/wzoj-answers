{ pkgs ? import <nixpkgs> { } }:
let
  my-python = pkgs.python3;
  python-with-my-packages = my-python.withPackages (p: with p; [
    # language server
    python-lsp-server
    python-lsp-black
    pyls-isort
    pylsp-mypy

    # package
    black
  ]);
in
pkgs.mkShell {
  buildInputs = [
    python-with-my-packages
  ];
}
