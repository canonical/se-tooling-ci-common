# Shared Config for SE Tooling Common Tasks

Code that follows a set of recognised standards and processes is easier to maintain and contribute to.

To align how standards and process are implemented across projects, this repository provides common resources for configuring tests, linting, packaging etc. Projects can then integrate them without having to implement their own versions from scratch.

The content of this repository takes two principle forms; language specific and language agnostic resources. For example it contains test config and github workflows for Python and Go projects as well as github workflows that work with any language.

The current implementation for Python is based on [pylint](https://www.pylint.org/) and [tox](https://tox.wiki/) which are commonly used tools many Python projects e.g. [OpenStack](https://www.openstack.org/). There are of course other tools that can replace these and we will aim to periodically review alternatives.

The basic structure is formed around providing *optional* and *recommended* resources whereby the latter is widely adopted across projects we maintain (and hopefully useful for others).


```
├── common
│   └── github_workflows
│   │   └── <generally applicable and language agnostic workflows>
├── go
│   ├── github_workflows
│   │   └── <generally applicable workflows for golang apps>
│   ├── optional
│   │   └── <optional config for golang apps linting, build, test etc>
├── python
│   ├── github_workflows
│   │   └── <generally applicable workflows for python apps>
│   ├── optional
│   │   └── <optional config for python apps linting, build, test etc>
│   └── recommended
│       └── <recommended config for python apps linting, build, test etc>
```
