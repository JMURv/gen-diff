### Hexlet tests and linter status:
[![Actions Status](https://github.com/JMURv/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/JMURv/python-project-50/actions)
[![linter-and-tests](https://github.com/JMURv/python-project-50/actions/workflows/linter-and-tests-check.yml/badge.svg)](https://github.com/JMURv/python-project-50/actions/workflows/linter-and-tests-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/c7a14c1587d0e99b8b2e/maintainability)](https://codeclimate.com/github/JMURv/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c7a14c1587d0e99b8b2e/test_coverage)](https://codeclimate.com/github/JMURv/python-project-50/test_coverage)
____
### About:

With this utility you can see a difference between two files with dict-like structure.
It accepts json and yml formats.
____
## HOW TO:

Use ```gendiff -h``` to get some help

Use ```gendiff path_to_file_1 path_to_file_2``` to run difference

## Different outputs:
You can use three formats:

| Formats              |                            Commads                            | Example                                                                                                                                                    |
|:---------------------|:-------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Stylish (default) | ``` gendiff --format stylish path_to_file_1 path_to_file_2``` | {<br/>- follow: false<br/>+ timeout: 20<br/>- proxy: 123.234.53.22<br/>}                                                                                   |
| 2. Plain             |  ``` gendiff --format plain path_to_file_1 path_to_file_2```  | Property 'common.follow' was added with value: true<br/>Property 'common.setting' was removed<br/>Property 'group.foobar' was updated. From 'foo' to 'bar' |
| 3. Json              |  ``` gendiff --format json path_to_file_1 path_to_file_2```   | {"setting": {"action": "not changed", "value": "foobar"}}                                                                                                  |

## Interactive examples

### .json flat 
[![asciicast](https://asciinema.org/a/6gam8V1DP5ADesSuv3YXkNrk2.svg)](https://asciinema.org/a/6gam8V1DP5ADesSuv3YXkNrk2)

### .yml flat
[![asciicast](https://asciinema.org/a/DI03BcoTpo8TCFv1AyRuoCEdd.svg)](https://asciinema.org/a/DI03BcoTpo8TCFv1AyRuoCEdd)

### .json nested
[![asciicast](https://asciinema.org/a/sZLE9c8S1exDql1MskVJhOCV9.svg)](https://asciinema.org/a/sZLE9c8S1exDql1MskVJhOCV9)

### Plain output
[![asciicast](https://asciinema.org/a/XxMXFGOaUoCscrUWKHXL42Fi0.svg)](https://asciinema.org/a/XxMXFGOaUoCscrUWKHXL42Fi0)

### JSON output
[![asciicast](https://asciinema.org/a/IH9GZsinqnRHzjX85CE8D3pVo.svg)](https://asciinema.org/a/IH9GZsinqnRHzjX85CE8D3pVo)