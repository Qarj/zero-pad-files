# zero-pad-files

Zero pad numbers in file names to make them two digits: Page1.pdf -> Page01.pdf

Use case example - you have 12 files named as follows

```
assign_10.pdf
assign_11.pdf
assign_12.pdf
assign_1.pdf
assign_2.pdf
assign_3.pdf
assign_4.pdf
assign_5.pdf
assign_6.pdf
assign_7.pdf
assign_8.pdf
assign_9.pdf
```

You want them to be named like this for processing in alphabetical order

```
assign_01.pdf
assign_02.pdf
assign_03.pdf
assign_04.pdf
assign_05.pdf
assign_06.pdf
assign_07.pdf
assign_08.pdf
assign_09.pdf
assign_10.pdf
assign_11.pdf
assign_12.pdf
```

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

Create symbolic link to create `zero` command in path

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
