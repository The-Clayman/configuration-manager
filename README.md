# configuration-manager

The configuration manager is a micro service design to hold, manage and suppliy configuration sets, such as Json.

The configuration manager will hold configuraiton in a data folder (that can be mounted as volume), and provide those on demand via RestAPI.

 
 
 ### RestAPI:
 
 #### 1. Get version:
 
 Returns the version number
 
  ```bash
Get http://<host_op>:port/configuration_manager/v1/version
```
 
 Respose:
  ```json
{
  "message": "Configuration Manager, version:[1.0.0]"
}
```
 
 
 #### 2. Get file list:
 
 returns a list of files exist on the configuration-manager Data folder
 
  ```bash
Get http://<host_op>:port/configuration_manager/v1/files
```

Respose:
  ```json
{
  "message": "Available files: ['prop.json']"
}
```


#### 3. Get configuraiton file

returns a file content by given file name
  ```bash
Get http://<host_op>:port/configuration_manager/v1/file/<file_name>
```

Respose:
  ```json
{
    "version": "1.0.0",
    "build": "7.5.158",
    "port": 5000,
    "instnce_name": "Configuration Manager 3"
}
```

### Build commands

#### Image build:

On a machine with docker.io installed, run:

```bash
docker build -t configuration-manager:v1 .
```


#### Continer run:
 
 ```bash
docker run -d --name configuraion-manager -p 5000:5000 -v <data_path_on_host>:/Data configuration-manager:v1
```
