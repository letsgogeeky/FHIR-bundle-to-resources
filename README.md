# FHIR-bundle-to-resources

Convert a FHIR patient bundle resource into individual bundles.

Does not require any python packages to be installed. only Python 3.

### Output in current directory
```python
python main.py -i <input_FHIR_bundle> 
```
Example:
```python
$ python main.py -i example_patient.json
```

### Output in specific directory
```python
python main.py -i <input_FHIR_bundle> -o <output_dir>
```
Example:
```python
$ python main.py -i example_patient.json -o result
```
