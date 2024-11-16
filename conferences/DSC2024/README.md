# Financial Instrument Reference Data - Identifiers

## Prerequisites

### Docker installed

Ensure Docker is installed on your system. Docker is available for Windows, macOS, and Linux. Installation instructions can be found on the Docker [website](https://docs.docker.com/desktop/).

### PermID API key
The only prerequisite for this project is to obtain a permid API token. To do so:
1. Go to https://permid.org/
2. From the top right, click on register and follow the steps to complete your sign-up
3. Once completed, go back again to https://permid.org/ and sign in with your login credentials
4. Once signed in, from the top menu, click on APIs-> Display my API token and copy your key
5. In the file called *dockerfile*, assign your API key to the **ENV PERMID_API_KEY** environmental variable, e.g. **ENV PERMID_API_KEY=abcdefg123456789**


## Launch the container

1. Open a terminal and navigate to the /path/to/repo/conferences/ODSC2024


2. Build the image by running the following command

   `docker build -t reference-data .`


3. Start the container with the command

   `docker run -p 8888:8888 -v ./scripts:/project/scripts  reference-data`


4. Navigate to `http://127.0.0.1:8888/lab`

