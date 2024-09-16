# COCO2CREATEML

COCO to CreateML Converter

# Usage

```shell
usage: Convert Coco to CreateML format [-h] -i INPUT [-o OUTPUT]

options:
  -h, --help    show this help message and exit
  -i, --input=  input name of coco format json
  -o, --output= output name of CreateML format json(default: annotation.createml.json)
```

Run convert

```shell
python coco2createml.py -i <input_json_path> -o <output_json_path>
```
