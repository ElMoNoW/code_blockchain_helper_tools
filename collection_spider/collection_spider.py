import json
import os
import requests


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder created: {folder_path}")


def save_collection_info(collection_name):
    base_url = "https://wax.api.atomicassets.io/atomicassets/v1"

    # Get collection information
    collection_url = f"{base_url}/collections/{collection_name}"
    collection_response = requests.get(collection_url)
    collection_data = collection_response.json()

    # Save collection information as JSON
    output = {
        "Collection": collection_data
    }

    # Create folder and save as JSON file
    collection_folder = f"{collection_name}_data"
    create_folder_if_not_exists(collection_folder)
    output_file = os.path.join(collection_folder, "collection.json")
    with open(output_file, "w") as file:
        json.dump(output, file, indent=4)

    print("Collection information saved successfully.")


def save_schema_names(collection_name):
    base_url = "https://wax.api.atomicassets.io/atomicassets/v1"

    # Get schemas
    schemas_url = f"{base_url}/schemas?collection_name={collection_name}&page=1&limit=100"
    schemas_response = requests.get(schemas_url)
    schemas_data = schemas_response.json()
    all_schemas = schemas_data["data"]

    # Extract schema names
    schema_names = [schema["schema_name"] for schema in all_schemas]

    # Save schema names as JSON
    output = {
        "SchemaNames": schema_names
    }

    # Create folder and save as JSON file
    collection_folder = f"{collection_name}_data"
    create_folder_if_not_exists(collection_folder)
    output_file = os.path.join(collection_folder, "schema_names.json")
    with open(output_file, "w") as file:
        json.dump(output, file, indent=4)

    print("Schema names saved successfully.")


def save_template_ids(collection_name):
    base_url = "https://wax.api.atomicassets.io/atomicassets/v1"

    # Get templates
    templates_url = f"{base_url}/templates?collection_name={collection_name}&page=1&limit=100&order=desc&sort=created"
    templates_response = requests.get(templates_url)
    templates_data = templates_response.json()
    all_templates = templates_data["data"]

    # Extract template_ids
    template_ids = [template["template_id"] for template in all_templates]

    # Save template_ids as JSON
    output = {
        "TemplateIDs": template_ids
    }

    # Create folder and save as JSON file
    collection_folder = f"{collection_name}_data"
    create_folder_if_not_exists(collection_folder)
    output_file = os.path.join(collection_folder, "template_ids.json")
    with open(output_file, "w") as file:
        json.dump(output, file, indent=4)

    print("Template IDs saved successfully.")


def save_template_structure(collection_name):
    base_url = "https://wax.api.atomicassets.io/atomicassets/v1"

    # Load schema names from schema_names.json
    collection_folder = f"{collection_name}_data"
    schema_names_file = os.path.join(collection_folder, "schema_names.json")
    with open(schema_names_file) as file:
        schema_names_data = json.load(file)

    schema_names = schema_names_data["SchemaNames"]

    # Save structure for each schema
    for schema_name in schema_names:
        structure_url = f"{base_url}/templates?collection_name={collection_name}&schema_name={schema_name}&page=1&limit=100&order=desc&sort=created"
        #/schemas/{collection_name}/{schema_name}/structure"
        structure_response = requests.get(structure_url)
        structure_data = structure_response.json()

        # Create folder for schema if it doesn't exist
        schema_folder = os.path.join(collection_folder, "schemas")
        create_folder_if_not_exists(schema_folder)

        # Save structure as JSON file
        output_file = os.path.join(schema_folder, f"{schema_name}_structure.json")
        with open(output_file, "w") as file:
            json.dump(structure_data, file, indent=4)

    print("Schema structures saved successfully.")


def save_all_templates(collection_name):
    base_url = "https://wax.api.atomicassets.io/atomicassets/v1"

    # Load template IDs from template_ids.json
    collection_folder = f"{collection_name}_data"
    template_ids_file = os.path.join(collection_folder, "template_ids.json")
    with open(template_ids_file) as file:
        template_ids_data = json.load(file)

    template_ids = template_ids_data["TemplateIDs"]

    all_templates = []

    # Retrieve each template
    for template_id in template_ids:
        template_url = f"{base_url}/templates/{collection_name}/{template_id}"
        template_response = requests.get(template_url)
        template_data = template_response.json()

        all_templates.append(template_data)

    # Save all templates as JSON file
    output_file = os.path.join(collection_folder, "all_templates.json")
    with open(output_file, "w") as file:
        json.dump(all_templates, file, indent=4)

    print("All templates saved successfully.")


def display_possible_keys(collection_name):
    collection_folder = f"{collection_name}_data"
    all_templates_file = os.path.join(collection_folder, "all_templates.json")

    with open(all_templates_file) as file:
        all_templates_data = json.load(file)

    possible_keys = set()
    for template_data in all_templates_data:
        # Check if the template_data is a dictionary
        if isinstance(template_data, dict):
            # Iterate over the key-value pairs in the template_data
            for key, value in template_data.items():
                possible_keys.add(key)
                # Check if the value is a nested dictionary
                if isinstance(value, dict):
                    # Iterate over the keys in the nested dictionary
                    for nested_key in value.keys():
                        possible_keys.add(nested_key)

    print("Possible keys in the all_templates.json file:")
    for key in possible_keys:
        print(key)


def search_and_save_variables(collection_name, search_term):
    collection_folder = f"{collection_name}_data"
    all_templates_file = os.path.join(collection_folder, "all_templates.json")

    with open(all_templates_file) as file:
        all_templates_data = json.load(file)

    for template_data in all_templates_data:
        variables = {}
        for key, value in template_data.items():
            if search_term.lower() in str(key).lower():
                variables[key] = value

        if variables:
            # Create a folder for search term if it doesn't exist
            search_folder = os.path.join(collection_folder, "search_results")
            create_folder_if_not_exists(search_folder)

            # Save variables as JSON file
            output_file = os.path.join(search_folder, f"{search_term}.json")
            with open(output_file, "w") as file:
                json.dump(variables, file, indent=4)

    print("Search and save completed.")


def check_schema_structure(collection_name):
    base_url = "https://wax.api.atomicassets.io/atomicassets/v1"

    # Load schema names from schema_names.json
    collection_folder = f"{collection_name}_data"
    schema_names_file = os.path.join(collection_folder, "schema_names.json")
    with open(schema_names_file) as file:
        schema_names_data = json.load(file)

    schema_names = schema_names_data["SchemaNames"]

    for schema_name in schema_names:
        structure_url = f"{base_url}/schemas/{collection_name}/{schema_name}/structure"
        structure_response = requests.get(structure_url)
        structure_data = structure_response.json()

        print(f"\nSchema Name: {schema_name}")

        # Print structure information
        for field in structure_data["data"]["schema"]["fields"]:
            print(f"\nField Name: {field['name']}")
            print(f"Data Type: {field['type']}")
            print(f"Is Required: {field['required']}")
            if "ref" in field:
                print(f"Ref: {field['ref']}")
            if "constraints" in field:
                print("Constraints:")
                for constraint in field["constraints"]:
                    print(f"- {constraint['type']}")

        print("\n" + "=" * 30)


# Main function
def main():
    collection_name = input("Enter the collection name: ")

    # Save collection information
    save_collection_info(collection_name)

    # Save schema names
    save_schema_names(collection_name)

    # Save template IDs
    save_template_ids(collection_name)

    # Save template structure for each schema
    save_template_structure(collection_name)

    # Save all templates
    save_all_templates(collection_name)

    # Display possible keys in all_templates.json
    display_possible_keys(collection_name)

    # Search and save variables by key name
    search_term = input("Enter a search term: ")
    search_and_save_variables(collection_name, search_term)

    # Check schema structure
    check_schema_structure(collection_name)


if __name__ == "__main__":
    main()
