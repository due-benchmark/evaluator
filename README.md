# DUE Evaluator
The repository contains the evaluator covering all of the metrics required by tasks within the DUE Benchmark, i.e., set-based F1 (for KIE), ANLS (used in document VQA), accuracy (including variant used in WTQ), as well as group-based ANLS we proposed for KIE problems with structured output. 

## Usage
The `deval` command will be available after the package installation. Every time, it is required to provide input and output files (both in the [DU-Schema format](https://github.com/due-benchmark/du-schema)) using `-o` and `-r` parameters.

Other settings are task-specific and limited to metric (`-m`) and optional case-insensitiveness (`-i`). Recommended values of these are:

| Dataset                    | Metric                                        | Case insensitive              |
|----------------------------|-----------------------------------------------|-------------------------------|
| DocVQA, InfographicsVQA    | ANLS                                          | Yes                           |
| Kleister Charity, DeepForm | F1                                            | Yes                           |
| PapersWithCode             | GROUP-ANLS                                    | Yes                           |
| WikiTableQuestions         | WTQ                                           | No (handled by metric itself) |
| TabFact                    | F1 (obtained value will be equal to Accuracy) | No                            |
