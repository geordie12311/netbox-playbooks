import pynetbox 
import yaml 
import os 

data_file = "netbox_initial.yaml"

with open(data_file) as f: 
    data = yaml.safe_load(f.read())

nb_url = os.getenv("NETBOX_URL")
nb_token = os.getenv("NETBOX_TOKEN")

nb = pynetbox.api(url=nb_url, token=nb_token)

interface_modes = nb.dcim.choices()["interface:mode"]
interface_mode = {
    "Access": 100, 
    "Tagged": 200, 
    "Tagged All": 300,
}
