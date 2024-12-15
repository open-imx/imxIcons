# Contributing to ImxIcons

First off ❤️ ️ ️thanks for taking the time to contribute! 

All types of contributions are encouraged and valued!!! Please make sure to read the relevant section before making your contribution.
It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions.

## Icon Creation
If you just create new icons, we’d love to include them in the library so you don’t have the hassle of implementing them yourself.
Feel free to share your icons by sending them through Discord or by creating a GitHub issue, and we’ll take care of the integration.

If you need any help or have questions along the way, don't hesitate to reach out to our dedicated Discord channel. We’re here to assist you!

Icons are built using individual SVG snippets, which we refer to as "parts." The library provides an easy way to assemble these parts into complete icons.
To give some insights on the process we have a page about adding icons to the library.

## Development

### Setup environment

We use [Hatch](https://hatch.pypa.io/latest/install/) to manage the development environment and production build. Ensure it's installed on your system.

```bash
hatch env create
```

#### Local environments
Make sure the IDE is using the created environment.

[Hatch configuration](https://hatch.pypa.io/1.0/config/hatch/):
>
> Configuration for Hatch itself is stored in a `config.toml` file located by default in one of the following platform-specific directories.
>
> | Platform | Path |
> | --- | --- |
> | macOS | `~/Library/Application Support/hatch` |
> | Windows | `%USERPROFILE%\AppData\Local\hatch` |
> | Unix | `$XDG_CONFIG_HOME/hatch` (the [XDG_CONFIG_HOME](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html#variables) environment variable default is `~/.config`) |
>
> If you wanted to store virtual environments in a .venv directory within your home directory, you could specify the following in the `config.toml`:
>
> ```toml
> [dirs.env]
> virtual = ".venv"
> ```

### Run unit tests

You can run all the tests with:

```bash
hatch run test
```

### Format the code

Execute the following command to apply linting and check typing:

```bash
hatch run lint
```

### Publish a new version

You can bump the version, create a commit and associated tag with one command:

```bash
hatch version patch
```

```bash
hatch version minor
```

```bash
hatch version major
```

Your default Git text editor will open so you can add information about the release.


## Serve the documentation

You can serve the Mkdocs documentation with:

```bash
hatch run docs-serve
```

It'll automatically watch for changes in your code.

## GitHub Actions Workflow

This repository uses GitHub Actions to automate tasks like testing, building documentation, and releasing packages. 
Below is an explanation of what happens when you push to a branch or create a pull request.

## Workflow Triggers and Actions

### Push to `feature` Branches
When code is pushed to a branch other than `main` the build workflow (`build.yml`) runs:
- **Testing**: Executes tests across multiple Python versions.
- **Linting and Type Checking**: Validates code compliance with linting rules and type annotations.

*No deployment or documentation build is triggered for feature branch pushes.*

### Push to `main` Branch
When code is pushed to the `main` branch (e.g., after merging a pull request) 2 workflows will be triggered.

The documentation workflow (`documentation.yml`):
- **Build**: Generates project documentation using Hatch.
- **Deploy**: Deploys the generated documentation to GitHub Pages.

The release workflow (`pre-release.yml`):
- **Testing and Linting**: Similar to the Build workflow, tests and lint checks are run across multiple Python versions.
- **Publishing**: Creates a GitHub pre-release with distribution artifacts.

### Release 
To release a new version of the application:
- Ensure the version has been appropriately updated prior to the pre-release. Use versioning tools mentioned above.
- Manually publish the release to make it available to users.

The release workflow (`release.yml`) is triggered when a release is published on GitHub:
  - Publishes the package to PyPI.
  - Code Coverage will be published on codecov.com. 
  - Triggers a release event in the related repository (`open-imx/imxIconsApi`).

This setup ensures rigorous testing and smooth deployment processes, while keeping workflows efficient for feature branch development.

## Styleguides

Todo

### Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* Consider starting the commit message with an applicable emoji: [https://gitmoji.dev/](https://gitmoji.dev/)

## Code of Conduct

This project and everyone participating in it is governed by the
[Code of Conduct](https://xxxxxx).
By participating, you are expected to uphold this code. Please report unacceptable behavior
to <>.
