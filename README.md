# Functional Dependencies Validation in CSS325 Database System

This project provides a Python script for validating functional dependencies in a database schema. The script checks for compliance with various normal forms, including 1NF, 2NF, 3NF, and BCNF.

## Overview

The script takes a database schema in JSON format as input and performs the following validations:

1. **1NF (First Normal Form):**
   - Ensures that attributes are atomic, and there are no repeating groups.

2. **2NF (Second Normal Form):**
   - Validates that all non-prime attributes are fully functionally dependent on the primary key.

3. **3NF (Third Normal Form):**
   - Checks for the absence of transitive dependencies.

4. **BCNF (Boyce-Codd Normal Form):**
   - Verifies that each non-trivial functional dependency is a super key.


