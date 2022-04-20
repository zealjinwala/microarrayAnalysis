# importing packages
import GEOparse
import pandas as pd
import numpy
import sys,os
import seaborn
import math

# 1. create a venv
# 2. pip install everthing
# 3. freeze > requirements.txt
# 4. write .py instead .ipynb
# 4. direct plots to a new dir
# 6. a make file to clean dirs/data, .gitignore
# 7. readme.md



# ------------- download and parse geodata
gse = GEOparse.get_GEO(geo="GSE17257", destdir='./data')
# TODO: this will download data everytime this section is executed. Can you optimize?
gsm= list(gse.gsms.values())[0]
gsm.metadata
# Data for each GSM is available in gse.gsms[...].table
# Combine GSM's into a single data table.
gsedata = None
for gsmid in gse.gsms.keys():
    gsmdata = gse.gsms[gsmid].table.rename(columns={'VALUE':gsmid})
    if gsedata is None: gsedata=gsmdata
    else:
        assert(gsedata['ID_REF'].equals(gsmdata['ID_REF'])) #just make sure that the same probes are listed in the same order.
        gsedata = pd.concat([gsedata,gsmdata[gsmid]],axis=1)

gsedata = gsedata.set_index('ID_REF')
gsedata.head()# Combine GSM's into a single data table.
gsedata = None
for gsmid in gse.gsms.keys():
    gsmdata = gse.gsms[gsmid].table.rename(columns={'VALUE':gsmid})
    if gsedata is None: gsedata=gsmdata
    else:
        assert(gsedata['ID_REF'].equals(gsmdata['ID_REF'])) #just make sure that the same probes are listed in the same order.
        gsedata = pd.concat([gsedata,gsmdata[gsmid]],axis=1)

gsedata = gsedata.set_index('ID_REF')
gsedata.head()
gplid = list(gse.gpls.values())[0]
print(gplid)
gpl = list(gse.gpls.values())[0].table
gpl[["ID", "Gene Symbol", "Gene Ontology Biological Process", "Gene Ontology Cellular Component", "Gene Ontology Molecular Function"]].head()

# ------------- data analysis
# t-test
# fold changes
# k-means clustering
# principle component analysis
# gene set enrichment

# ------------- The top 10 most different genes between the two groups
# ------------- Hierarchical clustering of samples
# ------------- Show a clustergram (heatmap, combined with clustering of samples and clustering of genes) of expression values.
