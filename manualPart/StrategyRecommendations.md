The automated test suite currently focuses on two critical scenarios:
1. Successful bet placement through the UI.
2. Successful bet placement through the API.

Bet placement is the application's main business flow and directly affects
the user's balance. Failures in this area may cause financial loss, refund
requests, and loss of customer trust.

Manual testing should focus on areas that are difficult to validate reliably
through automation:

- Visual layout and responsive design
- Usability and accessibility
- Exploratory testing
- Error-message clarity
- One release-level happy-path check

Moreover, while writing test cases, I found that there is no backend validation for charging money from
balance this is a potentially critical business defect. Currently we can make a bet through API with when user have negative balance. 

I would recommend to move to Docker to have same environment where we running tests this will decrease flaky tests when reason is different environment. 
Divide all test cases on suites for different stages of development like PR, Merge, Nightly, Release. PR we will trigger 
on each PR, should include Unit tests and API validation tests Merge should include API tests and UI smoke tests. Nightly 
should include all API and UI test cases. Release - should include all UI and API test cases and also manual tests and 
cross-browser check. Add method to change balance or add more users for tests (for example add creating of new user before test) 
right now we are using only 1 user and balance will be 0 after some execution we should handle this to make tests independent.
Pay more attention for API tests because there is potential critical issues with backend validation.  