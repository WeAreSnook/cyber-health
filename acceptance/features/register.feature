Feature: Register

Scenario: Sad path - Council already registered
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
And I click the "register" link
And I use an email address using a domain that is a subsequent user related to a council in the CyberHealth framework
And I fill in the other details with valid information
And I click on the "Sign Up" button
Then I see a warning that I cannot register "There is already a user for your local council." 

Scenario: Sad Path - Weak password
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
And I click the "register" link
And I use an email address using a domain that is a subsequent user related to a council in the CyberHealth framework
And I provide a weak password
And I fill in the other details with valid information
And I click on the "Sign Up" button
Then I see a warning that I cannot register "This password is too short. It must contain at least 8 characters." 

Scenario: Sad path - Email address previously registered
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
And I click the "register" link
And I provide an email address using a domain that was previously registered and password and click register
And I fill in the other details with valid information
And I click on the "Sign Up" button
Then I see a warning that I cannot register "There is already a user for your local council."