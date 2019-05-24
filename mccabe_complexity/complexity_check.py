import argparse
import subprocess


GIT_HASH_CMD = 'git ls-files --stage'.split()

COMPLEXITY_LEVEL = 12
CC_CMD = 'flake8 --max-complexity {complexity_level} {file}'


def get_lines(stdout_text):
    """Assumes your console uses utf-8"""
    return stdout_text.strip().decode('utf-8').split('\n')


def get_python_changes(git_command):
    """Returns python filenames which are staged"""
    python_changes = get_lines(subprocess.check_output(git_command.split()))
    return [s for s in python_changes if s.endswith('.py')]


def check_line_complexity(file_name):
    pipe = subprocess.Popen(
        CC_CMD.format(complexity_level=COMPLEXITY_LEVEL, file=file_name).split(),
        stdout=subprocess.PIPE,
    )
    out, _ = pipe.communicate()
    error_lines = [i for i in get_lines(out) if 'C901' in i]
    return '\n'.join(error_lines) if len(error_lines) > 0 else None


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to skip')
    parser.add_argument('--base_branch', nargs='?')
    args = parser.parse_args(argv)

    base_branch = 'master' if args.base_branch is None else args.base_branch
    git_changes_cmd = 'git diff {base_branch} --name-only --cached --diff-filter=ACM'.format(base_branch=base_branch)

    filename_list = get_python_changes(git_changes_cmd)
    if not filename_list:
        return 0

    clean_output_list = list(filter(lambda x: x is not None, map(check_line_complexity, filename_list)))
    if not clean_output_list:
        return 0
    print('\033[91mCheck {count} files with McCabe Complexity failed (greater than {complexity})\033[0m'.format(
        count=len(filename_list), complexity=COMPLEXITY_LEVEL))
    print('\n'.join(clean_output_list))
    return 1


if __name__ == '__main__':
    exit(main())
