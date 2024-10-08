{pkgs}: {
  deps = [
    pkgs.chromedriver
    pkgs.chromium
    pkgs.playwright-driver
    pkgs.gitFull
    pkgs.geckodriver
  ];
}
