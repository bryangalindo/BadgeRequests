# Getting Started

0. Run `pipenv shell` in the root directory
1. Run `pipenv install` in the root directory
2. Create a `.env` file in `badgerequest\Data` with the variables containing your database information (See Cosmos Emulator Setup below).
3. `cd` into `badgerequest\Client` and run `npm install`
4. Run `npm run dev` from `badge-app\Client` to start Svelte on `localhost:5000`
5. Run `uvicorn main:app --reload` from `badgerequest\API` to start the API on `localhost:8000`
6. Run `pytest` from any parent directory of tests to perform the tests.

# TODO

1. Improve README (add emulator setup guide)
2. User and badge routes
3. Add Axios and cleanup Svelte application
4. More TODOs
