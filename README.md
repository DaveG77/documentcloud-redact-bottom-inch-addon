
# Redact Bottom Inch

This repository contains the Redact Bottom Inch add-on for DocumentCloud. 

## Files

### main.py

This file is part of the `python-documentcloud` library.

This file contains a base class `AddOn`, which implements shared functionality
for all DocumentCloud Add-Ons to use.  In most cases, you should not need to
edit this file.  You will subclass this class in `main.py`.

Upon initializing this class, it parses the JSON passed in as an argument, and
populates a number of member variables.

Example invocation:
```
python3 main.py --documents 123 --username "..." --password "..."
```

### main.py

This is the file to edit to implement your Add-On specific functionality.  You
should define a class which inherits from `AddOn` from `addon.py`.  Then you
can instantiate a new instance and call the main method, which is the entry
point for your Add-On logic.  You may access the data parsed by `AddOn` as well
as using the helper methods defined there.  The `HelloWorld` example Add-On
demonstrates using many of these features.

If you need to add more files, remember to instantiate the main Add-On class
from a file called `main.py` - that is what the GitHub action will call with
the Add-On parameters upon being dispatched.

### config.yaml

This is a YAML file which defines the data for the add-on It uses the [JSON Schema](https://json-schema.org/) format, but allows you to
use YAML for convenience.  

### requirements.txt

This is a standard `pip` `requirements.txt` file. 

### .github/workflows/run-addon.yml

This is the GitHub Actions configuration file for running the add-on.  It
references a reusable workflow from the
`MuckRock/documentcloud-addon-workflows` repository.  

### .github/workflows/update-config.yml

This is the GitHub Actions configuration file for updating the configuration
file.  It references a reusable workflow from the
`MuckRock/documentcloud-addon-workflows` repository.  This workflow sends a
`POST` request to DocumentCloud whenever a new `config.yaml` file is pushed to
the repository. 

### LICENSE

The license this code is provided under, the 3-Clause BSD License
