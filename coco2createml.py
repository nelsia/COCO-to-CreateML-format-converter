import argparse
import json


def make_parser():
    parser = argparse.ArgumentParser("Convert Coco to CreateML format")
    parser.add_argument("-i", "--input", type=str, help="input name of coco format json", required=True)
    parser.add_argument("-o", "--output", default="annotation.createml.json", help="output name of CreateML format json")

    return parser


def coco_to_createml(coco_json_path, output_path):
    with open(coco_json_path, 'r') as coco_file:
        coco_data = json.load(coco_file)

    # Mapping category ID and label name
    categories = {cat['id']: cat['name'] for cat in coco_data['categories']}

    # output CreateML data
    create_ml_data = []

    # Process annotations
    for image_info in coco_data['images']:
        image_annotations = {
            "image": image_info['file_name'],
            "annotations": []
        }

        # Extract annotation
        annotations = [ann for ann in coco_data['annotations'] if ann['image_id'] == image_info['id']]

        for ann in annotations:
            bbox = ann['bbox']
            x_center = bbox[0] + bbox[2] / 2
            y_center = bbox[1] + bbox[3] / 2
            width = bbox[2]
            height = bbox[3]

            annotation_data = {
                "label": categories[ann['category_id']],
                "coordinates": {
                    "x": x_center,
                    "y": y_center,
                    "width": width,
                    "height": height
                }
            }
            image_annotations["annotations"].append(annotation_data)

        create_ml_data.append(image_annotations)

    # Save CreateML format
    with open(output_path, 'w') as output_file:
        json.dump(create_ml_data, output_file, indent=4)

    print(f"Generated CreateML format json. named: {output_path}")


def main():
    args = make_parser().parse_args()
    coco_to_createml(args.input, args.output)


if __name__ == "__main__":
    main()
