from flow.domains import Domains
from flow.domain import Domain
from flow.api.apiUtil import Api
import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    apiUtils = Api(os.getenv("DEBUG"))
    print(Domains(apiUtils).get())
