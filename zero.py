#!/usr/bin/env python3
import re
import time
import os
import argparse
import sys
version = "0.1.0"


# Flags
OUTPUT_IMMEDIATELY = None
TRIAL_RENAME = None

# Globals
STDOUT = ''


def clear_globals_for_unittests():
    global STDOUT
    STDOUT = ''


def set_output_immediately(b):
    global OUTPUT_IMMEDIATELY
    OUTPUT_IMMEDIATELY = b


def set_trial_rename(b):
    global TRIAL_RENAME
    TRIAL_RENAME = b


def output(out):
    global STDOUT
    if (OUTPUT_IMMEDIATELY):
        unicode_output(out)
    else:
        STDOUT += out + "\n"


def unicode_output(out):
    # when printing directly to the windows console stdout, unicode errors tend to be ignored automatically
    # if the user redirects stdout to a file, unicode errors can occurr - this code outputs the best it can and flags errors in the output
    try:
        print(out, flush=True)
    except UnicodeEncodeError:
        try:
            print(out.encode('utf8').decode(sys.stdout.encoding))
        except UnicodeDecodeError:
            print(out.encode('utf8').decode(sys.stdout.encoding,
                                            errors='ignore') + ' <-- UnicodeDecodeError')


def zero(path):
    output('\n' + time.strftime('%X : ') +
           'Zero padding files at path ' + path + '\n')
    start_time = time.time()

    scanned_file_count = 0
    zero_pad_count = 0

    for entry in os.scandir(path):
        if entry.is_dir():
            continue

        scanned_file_count += 1
        zero_pad_count += zero_pad_file(entry)

    output('\n' + time.strftime('%X : ') + str(zero_pad_count) +
           ' files zero padded (' + str(scanned_file_count) + ' files scanned), in ' + str(round(time.time()-start_time, 3)) + ' seconds')

    return STDOUT


def zero_pad_file(entry):
    new_name = entry.name
    zero_pad_count = 0

    find_numbers = re.search(r'([0-9]+)', entry.name)
    if find_numbers:
        match = find_numbers.group(1)
        if len(match) == 1:
            zero_padded = '0' + str(match)
            # print(f'match is {match}')
            # print(f'zero padded is {zero_padded}')
            new_name = new_name.replace(match, zero_padded)

    new_path = os.path.dirname(entry.path) + '/' + new_name

    info = entry.path
    if new_name != entry.name:
        info = entry.path + ' -> ' + new_path
        zero_pad_count = 1
        if (not TRIAL_RENAME):
            os.rename(entry.path, new_path)

    output(info)
    return zero_pad_count


parser = argparse.ArgumentParser(
    description='Zero pad filenames at path containing a single digit sequence')
parser.add_argument('--path', dest='path', required=False,
                    action='store', help='Target path')
parser.add_argument('--version', action='version', version=version)
parser.add_argument('--delayed', action='store_true', dest='output_delayed',
                    default=False, help='Will display stdout at end instead of immediately')
parser.add_argument('--trial', action='store_true', dest='trial_move',
                    default=False, help='Displays files to move without actually moving them')

args = parser.parse_args()
set_output_immediately(not args.output_delayed)
set_trial_rename(args.trial_move)

if (args.path):
    zero(args.path)
    if (not OUTPUT_IMMEDIATELY):
        unicode_output(STDOUT)
    sys.exit()
