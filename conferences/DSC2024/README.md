# Financial Data APIs

## Prerequisites

### 1. Docker installed

Ensure Docker is installed on your system. Docker is available for Windows, macOS, and Linux. Installation instructions can be found on the Docker [website](https://docs.docker.com/desktop/).

### 2. PermID API key
1. Go to https://permid.org/
2. From the top right, click on register and follow the steps to complete your sign-up
3. Once completed, go back again to https://permid.org/ and sign in with your login credentials
4. Once signed in, from the top menu, click on APIs-> Display my API token and copy your key
5. In the file called *dockerfile*, assign your API key to the **ENV PERMID_API_KEY** environmental variable, e.g. **ENV PERMID_API_KEY=abcdefg123456789**

### 3. AlphaVantage API Key: 

Register for a free AlphaVantage API key using [this](https://www.alphavantage.co/support/#api-key) link.

### 4. FinancialModelingPrep API Key
Sign up for a free API key using [this](https://intelligence.financialmodelingprep.com/register) link. After registration, log in, click on "Dashboard" from the top menu, and find your API key there.

## Launch the Docker container

1. Open a terminal and navigate to the 

   `/path/to/repo/conferences/DSC2024`


2. Make sure that Docker is running on your machine

   The operating-system independent way to check whether Docker is running is to ask Docker, using the `docker info` command.
   The docker info command checks whether Docker is running by querying the Docker daemon for information. If the daemon is active, it returns system information. If it’s not running, the command fails, indicating that Docker isn't operational. This provides an OS-independent way to verify if Docker is running since it directly communicates with the Docker daemon, regardless of the underlying operating system.


3. Build the image by running the following command

   `docker build -t financial-apis .`


4. Start the container with the command

   `docker run -p 8888:8888 -v ./scripts:/project/scripts  financial-apis`


5. Navigate to `http://127.0.0.1:8888/lab`

