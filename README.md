# Shared CI and Testing config for SE Tooling

Code that follows a set of recognised standards and processes is easier to maintain and contribute to.

To align how standards and process are implemented across projects, this repository provides resources for configuring tests, linting, packaging etc that reflects the expectations and quality standards that we want from our code.

The content of this repository will take two principle forms; language specific and language agnostic resources. For example it will contain test config and github workflows for Python and Go projects as well as github workflows that work with any language.

The first pass at this repository takes a rigid structure where there are *optional* and *recommended* resources whereby all projects should aim to implement the latter as far as possible.

The current implementation for Python is based on pylint and tox which are commonly used tools in almost all Python projects we work with. There are of course other tools that can replace these and we can certainly consider those as replacements provided there is a good enough reason to do so.

