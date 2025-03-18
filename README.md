# CosmosDB Data Solver

## Overview
The CosmosDB Data Solver is a Streamlit application designed to facilitate the uploading of files to Azure CosmosDB. It provides a user-friendly interface for managing data uploads and configuring necessary settings for both CosmosDB and Azure OpenAI services.
Here is the link to a GUI for this - https://azure-cosmosdb-data-uploader.streamlit.app/

## Project Structure
```
cosmosdb-data-solver
│── home
│   └── CosmosDB-FileUploader.py
│── settings
│   ├── CosmosDB-Setup.py
│   └── AzureOpenAI-Setup.py
│── upload
│   └── File-Uploader.py
├── cosmosdb_data_solver.py
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd cosmosdb-data-solver
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
streamlit run cosmosdb_data_solver.py
```

## Configuration
- **CosmosDB Setup**: Configure your CosmosDB settings in `content/settings/CosmosDB-Setup.py`.
- **Azure OpenAI Setup**: Set up Azure OpenAI configurations in `content/settings/AzureOpenAI-Setup.py`.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
