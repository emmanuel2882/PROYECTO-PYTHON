import pandas as pd
from sodapy import Socrata

def consultar_api(departamento, municipio, cultivo, limit=200):
    client = Socrata("www.datos.gov.co", None)
    query = f"departamento={departamento}&municipio={municipio}&cultivo={cultivo}"
    results = client.get("ch4u-f3i5", limit=limit)
    df = pd.DataFrame.from_records(results)
    
    
    return df
