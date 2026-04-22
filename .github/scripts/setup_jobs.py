import json
import argparse


def _generate_jobs(arch, python_version, key=""):
    if python_version == "all":
        if "windows" in key and arch == "aarch64":
            python_versions = ["3.11", "3.12", "3.13", "3.14"]
        else:
            python_versions = ["3.10", "3.11", "3.12", "3.13", "3.14"]
    else:
        python_versions = [python_version]

    if arch is None:
        jobs = [{"python_version": pv} for pv in python_versions]
    else:
        jobs = [{"python_version": pv, "arch": arch} for pv in python_versions]
    return jobs


def _as_bool(value):
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


def _extend_jobs(jobs, key, arch, python_version):
    jobs.setdefault(key, [])
    jobs[key].extend(_generate_jobs(arch, python_version, key))


def main():
    parser = argparse.ArgumentParser(description="Setup GitHub Actions jobs based on user input")
    parser.add_argument("--event_type", type=str, required=True, help="GitHub event type (e.g., push, pull_request)")
    parser.add_argument("--python-version", type=str, default="3.14", help="Python version to build packages for")
    parser.add_argument("--windows-x86", default=False, help="Whether to build Windows packages for x86_64")
    parser.add_argument(
        "--windows-x86-msvc",
        default=False,
        help="Whether to build Windows packages for x86_64 using MSVC",
    )
    parser.add_argument(
        "--windows-arm-msvc",
        default=False,
        help="Whether to build Windows packages for aarch64 using MSVC",
    )
    parser.add_argument("--linux-x86", default=False, help="Whether to build Linux packages for x86_64")
    parser.add_argument("--linux-arm", default=False, help="Whether to build Linux packages for aarch64")
    parser.add_argument("--macos-x86", default=False, help="Whether to build macOS packages for x86_64")
    parser.add_argument("--macos-arm", default=False, help="Whether to build macOS packages for aarch64")
    parser.add_argument("--source", default=False, help="Whether to build source package")

    args = parser.parse_args()

    # Define the jobs based on user input
    jobs = {}

    if args.event_type == "pull_request":
        jobs = {
            "linux": [
                {"python_version": "3.14", "arch": "x86_64"},
                {"python_version": "3.14", "arch": "aarch64"}
            ],
            "windows-msvc": [
                {"python_version": "3.14", "arch": "x86_64"},
                {"python_version": "3.14", "arch": "aarch64"}
            ],
            "windows-msys2": [
                {"python_version": "3.14"},
            ],
            "macos": [
                {"python_version": "3.14", "arch": "x86_64"},
                {"python_version": "3.14", "arch": "aarch64"}
            ],
            "source": [
                {"python_version": "3.14"}
            ]
        }
    else:
        if _as_bool(args.windows_x86):
            _extend_jobs(jobs, "windows-msys2", "x86_64", args.python_version)
        if _as_bool(args.windows_x86_msvc):
            _extend_jobs(jobs, "windows-msvc", "x86_64", args.python_version)
        if _as_bool(args.windows_arm_msvc):
            _extend_jobs(jobs, "windows-msvc", "aarch64", args.python_version)
        if _as_bool(args.linux_x86):
            _extend_jobs(jobs, "linux", "x86_64", args.python_version)
        if _as_bool(args.linux_arm):
            _extend_jobs(jobs, "linux", "aarch64", args.python_version)
        if _as_bool(args.macos_x86):
            _extend_jobs(jobs, "macos", "x86_64", args.python_version)
        if _as_bool(args.macos_arm):
            _extend_jobs(jobs, "macos", "aarch64", args.python_version)
        if _as_bool(args.source):
            jobs["source"] = _generate_jobs(None, args.python_version)

    # Output the jobs as JSON
    print(json.dumps(jobs, indent=4))


if __name__ == "__main__":
    main()
