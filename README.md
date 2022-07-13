# logmapping

Mapping log statements to runtime logs

## Installation

```bash
$ pip install logmapping
```

## Usage

Map runtime logs to their underlying logging statements.
<br>
This tool is able to (1) create a representation of the logging statements that allows for comparisons with runtime logs, (2) generate the ground truth templates for runtime logs based on the discovered mapping. In the figure below we visualize the functionality of the tool, namely (1) mining logging statements, (2) mining variables present in logging statements, and (3) creating the mapping from runtime logs the underlying logging statements. <br>
<img width="1202" alt="logmapping_workflow" src="https://user-images.githubusercontent.com/60047427/178629314-a0c2b52d-878d-469d-8528-aefd41e4b428.png">


## Design

<img width="1604" alt="log_mapping_design" src="https://user-images.githubusercontent.com/60047427/178629086-8802a2bd-2c0e-4a34-a25f-99d37aa858ef.png">

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`logmapping` was created by Stefan Petrescu. It is licensed under the terms of the MIT license.

## Credits

`logmapping` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
