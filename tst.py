#!/usr/bin/env python2.6
# coding: utf-8
# (c) 2011-2012 Dalton Serey, UFCG

from __future__ import print_function
from __future__ import with_statement
import os
import sys
import glob
import time
import getopt
import shlex
import signal
import string
import getpass
import unicodedata

from datetime import datetime, date
from subprocess import Popen, PIPE

if sys.version_info < (2,6):
    sys.stdout.write("tst.py: requires python 2.6 or later\n")
    sys.exit(0)

# TODO: add structural evaluation of the program (bad smells)
#       - check textual code of program
#       - check whether common bad names are used
#       - check length of variable names
#       - check both horizontal and vertical spacing (?)
#       - check proper indentation (not use tabs)
#       - use of gets instead of indexing in dicts
#       - length of lines
#       - code organization (functions & classes before everything)
#       - indicate operators in line command or from test specs


def is_markup_line(line):
    return line[0:4] == "[===" and line.strip()[-4:] == "===]"


def read_until_markup_line(file):
    data = ""
    while True:
        line = file.readline()
        if line == "" or is_markup_line(line):
            break
        data += line
    return data, line


def read_tests_from_tst_file(tst_file):
    alltests = {}
    try:
        file = open(tst_file, "r")
    except IOError as e:
        print(e)
        sys.exit(1)

    data, line = read_until_markup_line(file)
    while line != "":
        testname = line.strip()[4:-4].strip()
        input, line = read_until_markup_line(file)
        
        output, line = read_until_markup_line(file)
        alltests[testname] = (input, output)

    tests = []
    for test in alltests.keys():
        tests.append(Test(tst_file, alltests[test][0], alltests[test][1]))

    return tests


class Test():

    def __init__(self, problem_id, input_data, output_data):
        self.name = problem_id
        self.operators = [strip_blanks, strip_accents, string.lower]
        self.problem_id = problem_id
        self.input = input_data
        self.output = output_data
        self.relaxed_output = self.relax(self.output)


    def relax(self, data):
        for op in self.operators:
            data = op(data)
        return data


def strip_blanks(s):
    for white in string.whitespace:
        s = s.replace(white,"")
    return s


def strip_accents(s):
    text = []
    nkfd_form = unicodedata.normalize('NFKD', unicode(s,'utf-8'))
    only_ascii = nkfd_form.encode('ASCII', 'ignore')

    return only_ascii


def help():
    print("""\
    tst.py [<options>] [<pattern>]

    If <pattern> is given, tst tests all files that match the
    pattern. Otherwise, all python files (except "asserts.py") in
    the current directory will be tested. Test files match
    'tst-<name>.in' and 'tst-<name>.out'. If no such files exist, tst
    checks for the existence of asserts.py. If it exists, python runs
    asserts.py linking it to the code under test.
    
    Options:
    -v, --verbose: print obtained and expected output for each non-success.
    
    -a, --all: test all submissions (default: test only last one).
    
    -d <datetime>, --from_date=<datetime>: test only submissions from
       datetime or newer.

    -r <row_number>, --from_row=<row_number>: test only submissions from
       row_number or after.
    
    -t <num>, --timeout=<num>: timeout test execution at num seconds.

    -l, --log: output log format.

    -h, --help: print this help.

    (c) 2011-2012 Dalton Serey
    """)


def usage():
    print("Usage: tst [options] [PATTERN]\nTry 'tst --help' for help.")


# timeout schema
class CutTimeOut(Exception):
    pass


def alarm_handler(signum, frame):
    raise CutTimeOut

signal.signal(signal.SIGALRM, alarm_handler)


# the testing function
def test_cut(cut, test, timeout=10):
    """
    Runs and tests the code under test.

    Arguments:
    cut -- file name of the CUT (code under test)
    test -- test object (see class Test above)
    timeout -- number of seconds to timeout execution (default 10)

    Returns a single character, that indicates the test result:
      "." -- program ran successfully and gave correct answer
      "*" -- program ran successfully; answer "almost" correct (read below)
      "f" -- failure; program ran successfully, but gave wrong answer
      "S" -- program was aborted with SyntaxError
      "T" -- timeout; program didn't stop before time limit
      "0" -- program was aborted with ZeroDivisionError
      "I" -- program was aborted because of IndentationError
      "N" -- program was aborted because of NameError
      "Y" -- program was aborted because of TypeError
      "E" -- program was aborted with some runtime error or crashed

    """
    args = ""
    command = shlex.split("python %s %s" % (cut,args))

    while True:
        process = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE) 
        # run the code
        signal.alarm(timeout) 
        try:
            test.stdoutdata, test.stderrdata = \
                    process.communicate(input=test.input)
            signal.alarm(0)      # reset the alarm
            process.wait()
            break
        except CutTimeOut:      # program did not stop within expected time
            process.terminate()
            test.result = "T"
            return
        except OSError:
            process.terminate()  # external error ocurred; must try again!
  
    if process.returncode != 0:
        # program produced an error during execution
        if "SyntaxError" in test.stderrdata:
            test.result = "S"
        elif "ZeroDivisionError" in test.stderrdata:
            test.result = "0"
        elif "IndentationError" in test.stderrdata:
            test.result = "I"
        elif "IndexError" in test.stderrdata:
            test.result = "X"
        elif "ValueError" in test.stderrdata:
            test.result = "V"
        elif "TypeError" in test.stderrdata:
            test.result = "Y"
        elif "NameError" in test.stderrdata:
            test.result = "N"
        else:
            test.result = "E" # generic runtime error
        return
  
    if test.output == test.stdoutdata:
        test.result = "."
    elif test.relaxed_output == test.relax(test.stdoutdata):
        test.result = "*"
    else:
        test.result = "f"


def grade_result(result):
    result = result.lower()
    num_tests = len(result)
    num_dots = result.count(".")
    num_asterisks = result.count("*")
    num_failures = result.count("f")
    num_errors = len(result) - (num_dots + num_asterisks + num_failures)
    
    grade = (10.0*num_dots + 7.0*num_asterisks) / num_tests

    return grade


def print_verbose_report(tests):
    """
    For each test that fails, print both expected and obtained output.
    """
    for t in tests:
        if t.result in ('*', 'f'):
            print( "// === %s (result: %s) ===" % (t.name, t.result) )
            print( "// --- input ---" )
            print( t.input )
            print( "// --- expected output ---" )
            print( t.output )
            print( "// --- obtained output ---" )
            print( t.stdoutdata )
        if t.result not in ('.', '*', 'f'):
            print( "// === %s (result: %s) ===" % (t.name, t.result) )
            print( "// --- obtained stderr ---" )
            print( t.stderrdata )


def get_cut_id(cut):
    if verbosity == 0:
        return cut.split("-")[0]
    if verbosity == 1:
        return cut
    if verbosity == 2:
        data = cut.split("-")[0].split("_")
        data.insert(0, str(read_row_number(cut)))
        data.append(read_timestamp(cut).strftime("%d/%m/%Y %H:%M:%S"))
        return ",".join(data) # row_num,stud_id,prob_id,subm_num,timestamp


def run_io_tests(cuts, tst_files, timeout):
    # TODO: get rid of all output produced here
    # TODO: create object to handle output and verbosity level
    tests = []
    for tst_file in tst_files:
        tests.extend(read_tests_from_tst_file(tst_file))

    for cut in cuts:
        cut_id = get_cut_id(cut)
        if verbosity < 2:
            print("[%s] " % cut_id, end="")
        if verbosity == 2:
            print("%s," % cut_id, end="")
        sys.stdout.flush() # this allows watch evolution test by test
        result = ""
        for test in tests:
            test_cut(cut, test, timeout=timeout)
            if verbosity < 2:
                print( test.result, end="" )
            if verbosity == 2:
                print( test.result, end="" )
            result += test.result
            sys.stdout.flush()
        if verbosity < 2:
            print( " (%.1f)" % grade_result(result) )
        if verbosity == 2:
            print( ",%.1f" % grade_result(result) )

        if verbosity == 1:
            print_verbose_report(tests)


def run_pyunit_tests(cuts, pyunit_file, timeout):
    # TODO: get rid of all output produced here
    # TODO: create object to handle output and verbosity level
    for cut in cuts:
        cut_id = get_cut_id(cut)
        if verbosity < 2:
            print("[%s] " % cut_id, end="")
        if verbosity == 2:
            print("%s," % cut_id, end="")
        sys.stdout.flush()
        if os.access("undertest.py",os.O_RDONLY):
            os.remove("undertest.py")
        if os.access("undertest.pyc",os.O_RDONLY):
            os.remove("undertest.pyc")
        os.link(cut, "undertest.py")
        command = shlex.split("python %s" % pyunit_file)
        process = Popen(command, stdout=PIPE, stderr=PIPE) 

        # run the code
        # TODO: extract this!
        signal.alarm(timeout)
        try:
            timeout_status = ""
            stdoutdata, stderrdata = process.communicate()
            signal.alarm(0) # reset the alarm
            process.wait()
            results = stderrdata.split("\n")[0]
            if stderrdata.strip().startswith("Traceback"):
                results = "%s" % stderrdata.split("\n")[-2].split(":")[0]
        except CutTimeOut: # program didn't stop within expected time
            process.terminate()
            stderrdata = "(Timeout)"
            results = "Timeout"

        if verbosity < 2:
            print(results, "(%.1f)" % grade_result(results))
        if verbosity == 2:
            print(results, ",%.1f" % grade_result(results))
        if verbosity == 1:
            print(stderrdata)


def read_timestamp(cut):
    with open(cut) as file:
        for line in file:
            if line.startswith("# [tstbox] timestamp"):
                timestamp = line.split("=")[1].strip()
                return datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S")

    return datetime(1970,1,1)


def remove_old_cuts(cuts, from_date):
    """
    Removes submission older than given days from cuts.
    """
    for i in range(len(cuts)-1, -1, -1):
        cut_date = read_timestamp(cuts[i])
        if cut_date < from_date:
            del cuts[i]


def read_row_number(cut):
    with open(cut) as file:
        for line in file:
            if line.startswith("# [tstbox] row_number"):
                return int(line.strip().split("=")[1])
    return float("infinity")


def remove_tested_cuts(cuts, min_row_number):
    """
    Removes cuts already tested (those below row_number).
    """
    for i in range(len(cuts)-1, -1, -1):
        cut_row_number = read_row_number(cuts[i])
        if cut_row_number < min_row_number:
            del cuts[i]


def keep_last_submission_only(cuts):
    """
    Remove older submissions of a student for a problem.
    Only the last submission should be tested.
    """
    last = {}
    for cut in cuts:
        submission_data = cut.split("-")[0].split("_")
        if len(submission_data) < 3:
            # cut name does not conform to downloaded file name format
            # test it anyway
            last[(cut,"1")] = (cut,1)
        else:
            student_id, problem_id, num_envio = submission_data
            if (student_id,problem_id) not in last or \
                last[(student_id, problem_id)][1] < int(num_envio):
                last[(student_id, problem_id)] = (cut, int(num_envio))

    return [cut for cut,versao in last.values()]



def main(argv=None):

    # default parameters
    global verbosity               # global conf var

    verbosity = 0
    tst_files = glob.glob("*.tst") # every .tst file is a test set
    timeout = 1                    # default run time limit in seconds
    last_submission_only = True    # test only last submission
    from_row = 1                   # by default, test all submissions
    from_date = datetime(1970,1,1) # initial date to consider
    mode = "student"               # supported modes = student, professor

    # treat args and options
    try:
        options = [ "help", "professor", "all", "timeout=", "from_row=",
                    "from_date=", "verbose", "log" ]
        opts, args = getopt.getopt(argv, "hpat:r:d:vl", options) 
    except getopt.GetoptError: 
        usage()
        return 1

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help()
            return 2
        if opt in ("-p", "--professor"):
            mode = "professor"
        if opt in ("-a", "--all"):
            last_submission_only = False
        if opt in ("-t", "--timeout"):
            timeout = int(arg)
        if opt in ("-r", "--from_row"):
            from_row = int(arg)
        if opt in ("-d", "--from_date"):
            if "-" in arg.strip():
                date_format = "%d/%m/%Y-%H:%M"
            else:
                date_format = "%d/%m/%Y"
            from_date = datetime.strptime(arg.strip(), date_format)
        if opt in ("-v", "--verbose"):
            verbosity = 1
        if opt in ("-l", "--log"):
            verbosity = 2

    # command line args = cut file name pattern
    cuts_pattern = "*%s*.py" % args[0]  if  args  else  "*.py"
    non_cuts = ["asserts.py", "undertest.py", "tst.py"]
    cuts = list(set(glob.glob(cuts_pattern)) - set(non_cuts))

    if mode == "student":
        # mode student

        # run stdio tests
        test_pairs = [ ( tst, glob.glob(tst.replace(".tst","*.py")) )
                       for tst in tst_files ]
        for tst,pys in test_pairs:
            cuts = pys
            tst_files = [tst]
            run_io_tests(cuts, tst_files, timeout)

        # run pyunit tests
        # TO DO: 
        #run_pyunit_tests(cuts, "asserts.py", timeout)

        return 0
    
    else:
        # mode professor

        # should tst test all submissions of a student?
        if last_submission_only:
            cuts = keep_last_submission_only(cuts)

        # remove older submissions
        remove_old_cuts(cuts, from_date)
        remove_tested_cuts(cuts, from_row)

        # choose testing mode (stdio or pyunit) and run tests
        if tst_files:
            run_io_tests(cuts, tst_files, timeout)
        elif os.access("asserts.py", os.O_RDONLY):
            run_pyunit_tests(cuts, "asserts.py", timeout)
        else:
            print("tst.py: no tests found in %s" % os.getcwd().split("/")[-1])
            print("Try 'tst.py -h' for help.")

        return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
