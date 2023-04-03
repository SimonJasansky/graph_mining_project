Final Project for Building and Mining Knowledge Graphs

The purpose of this reporsitory is to construct a knowledge graph on global mining. 

It includes data files, jupyter notebooks, and configuration files. 


Jupyter notebooks
 -00_download_data.ipynb: The two main datasets are downloaded
 -01_merge_production_landuse.ipynb: Merging the two main datasets with spatial joins
 -01a_extract_unique_entities.ipynb: Used to extract unique entities, such as unique companies, countries, or materials, from the merged dataset or from the original downloaded data
 -02_convert_to_KG.ipynb: The merged and extracted data, stored in csv files, is converted to a knowledge graph with the help of mapping files (RML)
 -03_add_DBpedia_to_KG.ipynb: Adds the sameAs linking triples to the knowledge graph obtained above. The linking triples were obtained from the SILK software
 -99_testing_sparql_queries.ipynb: The knowledge graph is loaded and sparql queries are tested.


folder manual_input_data:
 -the file ownership_cleaned.csv was manually adjusted from one of the original datasets, as there were some data errors in it. 


mapping files (folder mappings):
 -yarrrml_mapping.yml: original mapping file, is converted to RML with the MATEY online tool
 -rml_mapping_XXXXXXX.rml.ttl: rml mapping file to convert csv file to knowledge graph
 -config.ini: provides the configuration for the mapping files

folder linking_triples:
 -target_graph4: the target graph containing the sameAs linking triples, obtained from the Silk software. 

folder output:
 - kg_before_linking.ttl: the knowledge graph before linking it to DBpedia with the sameAs triples
 - kg_after_linking.ttl: the final knowledge graph that is linked to DBpedia with sameAs triples

 GADM_levels_combined.csv: a file with all the GADM regions and their GIDs, can be used to link GADM region names to the mines. 