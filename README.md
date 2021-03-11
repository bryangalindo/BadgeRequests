# Getting Started

0. Run `pipenv shell` in the root directory
1. Run `pipenv install` in the root directory
2. Create a `.env` file in `badgerequest\API` with your CONNECTION_STRING.
3. From the `API` directory, run `py setup.py` to setup the mock data in the database.
4. `cd` into `badgerequest\Client` and run `npm install`
5. Run `npm run dev` from `badgerequest\Client` to start Svelte on `localhost:5000`
6. Run `uvicorn main:app --reload` from `badgerequest\API` to start the API on `localhost:8000`
7. Run `pytest` from `badgerequest\API` to perform the tests.

# TODO

1. Improve README (add emulator setup guide)
2. User and badge routes
3. Add Axios and cleanup Svelte application
4. More TODOs
