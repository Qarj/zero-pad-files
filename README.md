# zero-pad-files

Zero pad numbers in file names to make them two digits: Page1.pdf -> Page01.pdf

## Usage

Trial mode:

```
zero --path test/set01 --trial
```

Rename the files:

```
zero --path test/set01
```

Version

```
zero --version
```

Delayed output - show STDOUT at end rather than immediate

```
zero --delayed
```

## Debian / Ubuntu installation

Clone project

```sh
mkdir ~/git
cd ~/git
git clone https://github.com/Qarj/zero-pad-files
```

Copy to path and activate

```sh
sudo ln -sf $HOME/git/zero-pad-files/zero.py /usr/local/bin/zero
zero --version
```

## Run the unit tests

```sh
cd $HOME/git/zero-pad-files
chmod +x test_zero.py
./test_zero.py
```
