import json
import argparse


def _generate_jobs(arch, python_version):
    if python_version == ["all"]:
        python_versions = ["3.10", "3.11", "3.12", "3.13", "3.14"]
    else:
        python_versions = [python_version]

    if arch is None:
        jobs = [{"python_version": pv} for pv in python_versions]
    else:
        jobs = [{"python_version": pv, "arch": arch} for pv in python_versions]
    return jobs


def main():
    parser = argparse.ArgumentParser(description="Setup GitHub Actions jobs based on user input")
    parser.add_argument("--event_type", type=str, required=True, help="GitHub event type (e.g., push, pull_request)")
    parser.add_argument("--python-version", type=str, default="3.14", help="Python version to build packages for")
    parser.add_argument("--windows-x86", default=False, help="Whether to build Windows packages for x86_64")
    parser.add_argument("--windows-arm", default=False, help="Whether to build Windows packages for aarch64")
    parser.add_argument("--windows-x86-msvc", default=False, help="Whether to build Windows packages for x86_64 using MSVC")
    parser.add_argument("--windows-arm-msvc", default=False, help="Whether to build Windows packages for aarch64 using MSVC")
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
                {"python_version": "3.14", "arch": "x86_64"},
                {"python_version": "3.14", "arch": "aarch64"}
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
        if args.windows_x86:
            jobs["windows-msys2"] = _generate_jobs("x86_64", args.python_version)
        if args.windows_arm:
            jobs["windows-msys2"] = _generate_jobs("aarch64", args.python_version)
        if args.windows_x86_msvc:
            jobs["windows-msvc"] = _generate_jobs("x86_64", args.python_version)
        if args.windows_arm_msvc:
            jobs["windows-msvc"] = _generate_jobs("aarch64", args.python_version)
        if args.linux_x86:
            jobs["linux"] = _generate_jobs("x86_64", args.python_version)
        if args.linux_arm:
            jobs["linux"] = _generate_jobs("aarch64", args.python_version)
        if args.macos_x86:
            jobs["macos"] = _generate_jobs("x86_64", args.python_version)
        if args.macos_arm:
            jobs["macos"] = _generate_jobs("aarch64", args.python_version)
        if args.source:
            jobs["source"] = _generate_jobs(None, args.python_version)

    # Output the jobs as JSON
    print(json.dumps(jobs, indent=4))


if __name__ == "__main__":
    main()
