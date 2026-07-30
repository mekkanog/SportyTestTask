ID - TestFoot1 \
Title - Verify successful placement on a single bet \
Priority: Critical \
Risk Rationale: Main business logic of application is betting.\
Steps: \
1) Open Application https://qae-assignment-tau.vercel.app/?user-id=<User-ID>
2) Find any valid record with upcoming match 
3) Make a bet on any result. 
4) Enter valid value in “Stake” field 
5) Click on “Place bet” button
Expected Result: Modal window with “Bet Placed Successfully” should appear. Modal window should contain “Bet ID”, 
“Match details”, “Selection”, “Stake”, “Odds”, “Potential payouts”, “Placement timestamp”. User balance should be
reduced on stake amount

ID - TestFoot2 \
Title - Verify that the user cannot place a bet with a negative stake \
Priority: Critical \
Risk Rationale: User should not have possibility to make negative stake this can break balance functionality \
Steps: \
1) Open Application https://qae-assignment-tau.vercel.app/?user-id=<User-ID>
2) Find any valid record with upcoming match
3) Make a bet on any result.
4) Enter negative value “Stake” field. For example (-10)
5) Click on “Place bet” button 
Expected Result: Validation error message should appear. Bet placement should be blocked. No bet placement request 
should be sent. Balance should remain unchanged.

ID - TestFoot3 \
Title - Check that rebet functionality is working.  \
Priority: High \
Risk Rationale: Rebet functionality should work properly and send the same data which was specified by user before the error. \
Steps: \
1) Open Application https://qae-assignment-tau.vercel.app/?user-id=<User-ID>
2) Find any valid record with upcoming match
3) Make a bet on any result.
4) Enter valid value “Stake” field. For example 5 
5) Switch browser to offline mode 
6) Click on “Place bet” button
7) After error modal appear switch browser to online mode again. 
8) Click on "Rebet" button
Expected Result: Success window should appear this window should contain the same values that user select and enter before. \

ID - TestFoot4 \
Title - Verify stake amount boundaries \
Priority: High \
Risk Rationale: User should not be able to enter values more or less that application stake range. \
Steps:
1) Open Application https://qae-assignment-tau.vercel.app/?user-id=<User-ID>
2) Find any valid record with upcoming match
3) Make a bet on any result.
4) Enter value which is out of the range of possible values "0.99" “Stake” field. 
5) Repeat step 4 with different value "100.01"
Expected Result: Validation error message should appear, "Place bet" button should be disabled and not interactable. \
Comment: In specification requirements are not clear. On Business rule there is minimum bet 1.00 EUR  on Validation Rules 1.01 EUR \

ID - TestFoot5 \
Title - Check that user are not able to make double bet \
Priority: High \
Risk Rationale: User should not be able to make a double bet \
Steps: \
1) Open Application https://qae-assignment-tau.vercel.app/?user-id=<User-ID>
2) Find any valid record with upcoming match
3) Make a bet on any result.
4) Enter valid value in "Stake" field
5) Make doubleclick on "Place bet" button 
Expected Result: Only one bet should be successfully created and the balance should be deducted once. Application should \
prevent duplicate bet placement.

ID - TestFoot6 \
Title - Check that filtering for match list is working \
Priority: Medium \
Risk Rationale: User should see data according to select date filter. \
Steps: \
1) Open Application https://qae-assignment-tau.vercel.app/?user-id=<User-ID>
2) Click on "Date" filter button 
3) Select date from date picker. 
4) Click on "Apply" button
Expected Result: Records in table should show only matches which are going on the picked date \

