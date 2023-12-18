import json

def is_1nf(schema):
    attributes = set(schema.get("attributes", []))
    functional_dependencies = schema.get("functional_dependencies", [])
    super_keys = [set(key) for key in schema.get("super_keys", [])]
    primary_key = set(schema.get("primary_key", []))

    # Check if the primary key is a super key
    if not any(attr in set(primary_key) for super_key in super_keys for attr in super_key):
        return False

    # Check if each functional dependency is valid
    for fd in functional_dependencies:
        lhs, rhs = set(fd["lhs"]), set(fd["rhs"])

        # Check if the left-hand side (lhs) is a subset of super keys
        if not any(lhs.issubset(super_key) for super_key in super_keys):
            return False

        # Check if the right-hand side (rhs) is a subset of attributes
        if not rhs.issubset(attributes):
            return False

    return True

def is_2nf(schema):
    if not is_1nf(schema):
        return False

    # Check if all non-prime attributes are fully functionally dependent on the primary key
    non_prime_attributes = set(schema.get("attributes", [])) - set(schema.get("primary_key", []))
    functional_dependencies = schema.get("functional_dependencies", [])
    primary_key = set(schema.get("primary_key", []))

    for attr in non_prime_attributes:
        if not is_fully_dependent(attr, functional_dependencies, primary_key):
            return False

    return True

def is_fully_dependent(attribute, functional_dependencies, primary_key):
    for fd in functional_dependencies:
        if attribute in fd["rhs"]:
            lhs = set(fd["lhs"])
            # Check if the left-hand side (lhs) is a subset of the entire primary key
            if not lhs.issubset(primary_key):
                return False
    return True

def is_3nf(schema):
    if not is_2nf(schema):
        return False

    # Check if all transitive dependencies are removed
    for fd in schema.get("functional_dependencies", []):
        lhs, rhs = set(fd["lhs"]), set(fd["rhs"])

        # Check if the left-hand side (lhs) is a super key or a key
        if not any(lhs.issubset(super_key) for super_key in schema.get("super_keys", [])):
            return False

        # Check if the right-hand side (rhs) is a subset of attributes
        if not rhs.issubset(set(schema.get("attributes", []))):
            return False

    return True

def is_bcnf(schema):
    if not is_3nf(schema):
        return False

    functional_dependencies = schema.get("functional_dependencies", [])
    super_keys = [set(key) for key in schema.get("super_keys", [])]

    # Check if each non-trivial functional dependency is a super key
    for fd in functional_dependencies:
        lhs, rhs = set(fd["lhs"]), set(fd["rhs"])

        # Check if the left-hand side (lhs) is a super key
        if not any(lhs.issuperset(super_key) for super_key in super_keys):
            return False

    return True


def main():
    # Get the database schema from the user
    schema_file = input("Enter the path to the JSON file containing the database schema: ")
    
    try:
        with open(schema_file, "r") as f:
            schema = json.load(f)
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
        return
    except json.JSONDecodeError:
        print("Invalid JSON format. Please provide a valid JSON file.")
        return

    # Validate 1NF
    result_1nf = is_1nf(schema)

    # Validate 2NF
    result_2nf = is_2nf(schema)

    # Validate 3NF
    result_3nf = is_3nf(schema)

    # Validate BCNF
    result_bcnf = is_bcnf(schema)

    # Output the result
    if result_1nf:
        print("The given schema satisfies 1NF.")
    else:
        print("The given schema does not satisfy 1NF.")

    if result_2nf:
        print("The given schema satisfies 2NF.")
    else:
        print("The given schema does not satisfy 2NF.")

    if result_3nf:
        print("The given schema satisfies 3NF.")
    else:
        print("The given schema does not satisfy 3NF.")

    if result_bcnf:
        print("The given schema satisfies BCNF.")
    else:
        print("The given schema does not satisfy BCNF.")

if __name__ == "__main__":
    main()
