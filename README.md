# THIS REPO IS DEPRICATED AND ONLY SUPPORTS TABLASSERT 3.1.3

See [Tablassert 4.3.0](https://github.com/SkyeAv/Tablassert/tree/4.3.0) for updated config stores and checkers. The configs are now in a submodule.

# MultiomicsKG (1.0.2)

## Skye Goetz, Gwênlyn Glusman, and the Catrax Team

Here are the configs for MultiomicsKG. Feel free to add or edit any of these as you see fit. There's a config checker and guidelines here too. **Some configs are now written by programs.**

### Usage (Unix)

*First Install the Utility as a Module*

```bash
pip install -e <path_to_CONFIG_CHECKER>
```

To Test a KG Config

```bash
kg_config <path_to_kg_config>
```

To Test a Table Config

```bash
table_config <path_to_table_config>
```

Unittests

```bash
config_checker_test
```

### KG Config Usage

```yaml
knowledge_graph_name :
vesion_number : # Must be a string like '1.0.0'
max_workers : # Max Parallel Processes
p_value_cutoff : # Max P Value
progress_handler_timeout : # For all SQL Databases and Queries

config_directories:
 - # List of Directories That Contain Table Configs
 

override_sqlite : # Paths
supplement_sqlite : 
babel_sqlite : 
kg2_sqlite :
predicates_sqlite : 

confidence_model : # Pretrained Sklearn Linear Regression Model
tfidf_vectorizer : # Pretrained Sklearn TFIDF Vectorizer Model

pubmed_sqlite : 
```

### Table Config Usage

```yaml
# USE "~" FOR "None"

column_style: # alphabetic (A-ZZ), numeric (1-100), else normal

method_notes : # Addtional details describing the methodology of the tabular data

data_location :
 path_to_file : # <Path to the Supplemental Table, Absolute or Relative to Where You 
 # Execute the Script>
 delimiter : # ONLY if CSV, TSV, TXT File
 sheet_to_use : # ONLY if XLS or XLSX File
 first_line : # First Line to Use / ONLY if XLS or XLSX File
 last_line : # Last Line to Use / ONLY if XLS or XLSX File

provenance : 
 publication : # PMC/PMID/doi Identifier
 publication_name : # Paper Title
 authors : 
 year_published : 
 journal :
 table_url : # Valid URL Telling Tablassert Where to Download the Desired Table
 yaml_curator :
 curator_organization : 

subject :
 curie : # <A CURIE for the Entire Table>
 # value : <A Value for the Entire Table>
 # curie_column_name : <A Name of a Column Containing CURIEs>
 # value_column_name : <A Name of a Column Containing Values>
 # shared_curie_column : <A Name of a Column Containing CURIEs and Something  
  #Else You Want to Preserve>
 # shared_value_column : <A Name of a Column Containing Values and Something  
  #Else You Want to Preserve>
 expected_classes : # List
   - # biolink:Class
 classes_to_avoid : # List
   - # biolink:Class
 expected_taxa : # Only For biolink:Gene Filtering / List
   - # NCBITaxon:Taxon
 regex_replacements : # List
   - pattern :
     replacement : 

predicate : # biolink:Predicate

object :
 value_column_name : # Name of Column with Values
 prefix : # List
   - prefix : # Prefix
 suffix :
   - suffix : # Suffix
 explode_column  : # Delimeter to Split Values by Before Exploding to Separate Rows
 fill_values : # How to Fill Empty Values in Column (ffil or bfill)

reindex : # List 
  - mode : # Mode (greater_than_or_equal_to, less_than_or_equal_to,
      #equal_to, not_equal_to)
    column : #nGoes By Final Column Names ONLY if Column is Included in the     
      #Final KG
    value :

attributes : 
 p : # P-Value
   value : # <Attribute Value for Entire Table>
   # column_name : <Name of Column to Containing Attribute>
   math : # List
     - operation : # <Python math Module Attribute>
       parameter : # Optional: <Second Parameter for Attribute>
       order_last : # Optional: <yes/no About Whether to Order parameter Last>
        #order_last is Required when parameter is Specified (Vice-Versa)
 n : # Sample Size
 relationship_strength : # Field Describing the Strength of an Edge
 relationship_type : # Method for Strength
 p_correction_method : # Field Describing If/How P-Value was Corrected
 knowledge_level :
 agent_type :

sections : # Can List Multiple
 - # <Copy of Section Formatted Like the Rest of the Config Nested in A Sections Section> 
   # For example...
   # attributes :
     # p :
       # value :
   # object :
     # curie :
     # prefix :
       # - prefix :
```
